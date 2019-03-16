#Import Django Various Django Libraries including model of Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#Form for user registration, makes use of django auth forms. 
class UserRegisterForm(UserCreationForm):
    #Define an email field for email variables
    email = forms.EmailField()
    
    #For model user there are fields for username, email and password. This is in regards to user registration
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        #Form for user profile updates, makes use of django auth forms. 
class UserUpdateForm(forms.ModelForm):
    #Define a username field with a max character length of 50 characters
    username = forms.CharField(max_length=50)
    #For model profile there are fields for the account username. This is in regards to user registration
    class Meta:
        model = Profile
        fields = ['username']
