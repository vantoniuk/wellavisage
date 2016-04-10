from django import forms

class PictureForm(forms.Form):
	pic_file = forms.ImageField(label = 'select a picture',)
