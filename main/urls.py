from django.urls import path
from .views import user_profile

app_name = "register"
urlpatterns = [
    # path('register/', register, name="register"),
    path('user/<int:user_id>/profile', user_profile, name="userprofile"),
    path('login/',)
]