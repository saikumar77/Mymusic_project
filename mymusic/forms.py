from django import forms
from models import Userdetails

class UserDetailsForm(forms.ModelForm):
	class Meta:
		model = Userdetails
		fields = ('firstname', 'lastname', 'email', 'password', 'mobilenumber')