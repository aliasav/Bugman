from django import forms
from bug.models import Bug

class BugForm(forms.Form):
	title = forms.CharField(max_length=100, required=True)
	description = forms.CharField(max_length=600, required=False, widget=forms.TextInput(attrs={'placeholder': 'KISS! (keep-it-short-&-simple!)'}))
	link = forms.URLField(max_length=300, required=True, widget=forms.TextInput(attrs={'placeholder': 'URL of where the bug occured.'}))
	screenshot = forms.ImageField(required=False)
	guidelines = forms.CharField(widget=forms.Textarea, required=False)
	category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Bug.CATEGORY_LIST, required=True)
	priority = forms.ChoiceField(choices=Bug.PRIORITY_LIST, required=True)
	#assigned_developer
