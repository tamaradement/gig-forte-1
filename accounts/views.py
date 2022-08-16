from django.urls import reverse_lazy 
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class UpdateUserView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("home")
    template_name = "registration/update_user.html"

    def get_object(self, queryset=None): 
        return self.request.user

