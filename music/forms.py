from django import forms
from django.contrib.auth.models import User
#from music.models import Favorite


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# class FavoriteForm(forms.ModelForm):
#     class Meta:
#         model = Favorite
#         fields = ("song",)

#         def clean_song(self):
#             pass
