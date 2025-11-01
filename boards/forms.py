# boards/forms.py
from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
        }
