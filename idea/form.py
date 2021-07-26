from django.forms.widgets import Textarea
from idea.models import Idea
from django import forms

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'

        widgets = {
            'content': Textarea(attrs={}),
        }