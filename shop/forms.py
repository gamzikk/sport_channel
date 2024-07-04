from django import forms
from django.core import validators
from .models import Product


class CreateProductForm(forms.ModelForm):
	image = forms.FileField(widget=forms.FileInput(attrs={'class': 'input-reg'}))
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-reg', 'placeholder': 'Enter name'}))
	text = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-reg', 'placeholder': 'Enter text'}))
	price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-reg', 'placeholder': 'Enter price'}))

	class Meta:
		model = Product
		fields = ['image', 'name', 'text', 'price']