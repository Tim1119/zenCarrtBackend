from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm):

        model = User
        fields = ['email', 'full_name']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['email', 'full_name']
