from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Rating
from cloudinary.models import CloudinaryField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PostForm(forms.ModelForm):
    photo = CloudinaryField('image')

    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description', 'technologies',)



