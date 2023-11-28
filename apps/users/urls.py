from .api.v1.urls import urlpatterns as v1_urlpatterns

app_name = "users"


urlpatterns = []
urlpatterns += v1_urlpatterns
