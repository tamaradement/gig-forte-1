from django.urls import path
from .views import SignUpView, UpdateUserView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("update_user/", UpdateUserView.as_view(), name="update_user"),
]
