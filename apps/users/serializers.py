from django.db.models import Q
from rest_framework import serializers
from apps.users.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


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


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "phone_number"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate_email(self, value):
        user = self.context["request"].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError(
                {"email": "This email is already in use."}
            )
        return value

    def validate_username(self, value):
        user = self.context["request"].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError(
                {"username": "This username is already in use."}
            )
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["last_name"]
        instance.email = validated_data["email"]
        instance.username = validated_data["username"]

        instance.save()

        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    """change old password"""

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[
            RegexValidator(
                regex="^(?=(.*\d){1})(?=.*[a-zA-Z])(?=.*[!@#$%])[0-9a-zA-Z!@#$%]{8,}",
                message="password must contain numbers, letters, simbols and length greeter than 8",
                code="invalid change password",
            )
        ],
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
        user = self.context["request"].user
        if user.pk != instance.pk:
            raise serializers.ValidationError(
                {"authorize": "You dont have permission for this user."}
            )
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ConfirmPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        required=True,
        validators=RegexValidator(
            regex="^(?=(.*\d){1})(?=.*[a-zA-Z])(?=.*[!@#$%])[0-9a-zA-Z!@#$%]{8,}",
            message="password must contain numbers, letters, simbols and length greeter than 8",
            code="invalid change password",
        ),
    )
    confirm_password = serializers.CharField(required=True)
    uid = serializers.CharField(max_length=255, required=True)
