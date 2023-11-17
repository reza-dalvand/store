from django.contrib.auth.password_validation import validate_password
from django.db.models import Q
from rest_framework import serializers
from apps.users.models import User
from django.utils.translation import gettext_lazy as _


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        if User.objects.filter(Q(email=value) | Q(username=value)).exists():
            raise serializers.ValidationError(
                {"error": "Email or username in use already"}
            )
        return value

    def validate(self, validated_data):
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"error": _("passwords did not match")})
        return validated_data

    def create(self, validate_data):
        user = User.objects.create(
            email=validate_data["email"], username=validate_data["username"]
        )
        user.set_password(validate_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """email considered char field for check username and email together"""

    email = serializers.EmailField(max_length=256)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        user = User.objects.filter(Q(email=email) | Q(username=email)).first()
        if user and user.check_password(password):
            validated_data["user"] = user
            return validated_data
        raise serializers.ValidationError({"error": "user does not exist"})


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "phone_number"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": _("Password fields didn't match.")}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": _("Old password is not correct")}
            )
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()

        return instance


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, data):
        password = data["password"]
        password2 = data["password2"]

        if password != password2:
            raise serializers.ValidationError(
                {
                    "password2": _("passwords not match"),
                }
            )
        elif len(password) < 4:
            raise serializers.ValidationError(
                {"password2": _("password must be at least 4 characters")}
            )
        return data

    def prepare_user_account(self):
        self.user_account = User(
            username=self.validated_data["username"], email=self.validated_data["email"]
        )
        self.user_account.set_password(self.validated_data["password"])

    def save(self):
        self.prepare_user_account()
        self.user_account.save()
        return self.user_account


class ChangeForgetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
