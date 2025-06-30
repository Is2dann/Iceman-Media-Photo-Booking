from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # index.html loaded with autofocus on username field of the form.
    # this function disables it ("from stackoverflow")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})