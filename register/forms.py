from django import forms
from django.contrib.auth.forms import UserCreationForm
from Forum.models import User
from crispy_forms.helper import FormHelper


class SignUpForm(UserCreationForm):
	helper = FormHelper()
	helper.form_show_labels = False
	
	class Meta:
		model = User
		fields = ['username']