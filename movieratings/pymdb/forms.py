from django import forms
from django.contrib.auth.models import User
from .models import Rater, Rating


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class RaterForm(forms.ModelForm):
    class Meta:
        model = Rater
        fields = ('age', 'gender', 'occupation', 'zip_code')

class RatingForm(forms.ModelForm):
    # rater = forms.CharField(widget=forms.HiddenInput())
    # movie = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Rating
        fields = ('rating',) # 'rater', 'movie', 'rating')
