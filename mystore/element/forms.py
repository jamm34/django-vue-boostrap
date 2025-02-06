from django import forms
#from django.forms import ModelForm

from .models import Type, Category, Element



class ElementForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255, min_length=3)
    slug = forms.SlugField(label='Slug', max_length=255, min_length=3)
    description = forms.CharField(label='Description', initial='Content initial', widget=forms.Textarea)
    price = forms.DecimalField(label='Price', decimal_places=2, max_digits=5, required=True)
    type = forms.ModelChoiceField(label='Type', queryset=Type.objects.all(), initial=1)
    category = forms.ModelChoiceField(label='Category', queryset=Category.objects.all(), initial=2)


class ElementModelForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ('title', 'slug', 'description', 'price', 'type', 'category')
