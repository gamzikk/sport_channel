from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	comment_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-comment', 'placeholder': 'Введите текс комментария'}))

	class Meta:
		model = Comment
		fields = ['comment_text']