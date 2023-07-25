from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Forum.models import User, Author
from crispy_forms.helper import FormHelper


class SignUpForm(UserCreationForm):
	helper = FormHelper()
	helper.form_show_labels = False
	
	class Meta:
		model = User
		fields = ['username']
		

class LoginForm(AuthenticationForm):
	username = forms.CharField(max_length = 30,widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Username'}))
	password = forms.CharField(max_length = 30, widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Password'}))

    
class UpdateForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ['fullname', 'bio', 'profile_photo']
		

