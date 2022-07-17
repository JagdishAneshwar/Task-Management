from django import forms
from .models import member,task

class users(forms.ModelForm):
	class Meta:
		model = member
		fields = ['name', 'role', 'upload']

class tasks(forms.ModelForm):
	class Meta:
		model = task
		fields = ['name', 'desc', 'due']