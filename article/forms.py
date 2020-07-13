from django import forms
from .models import Post

class PostForm(foms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
