from django import forms
from .models import Post, Startup, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = 'Post'
        fields = '__all__'

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()

