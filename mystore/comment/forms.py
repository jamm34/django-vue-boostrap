from django.forms import ModelForm
from django import forms
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
    

# widget en forma de clase

class OtherWidget(forms.TextInput):
    class Media:
        css = {
            'all': ["pretty.css"],
            
        }
        js = ["animations.js", "actions.js"]