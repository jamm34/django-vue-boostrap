from django import forms

from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from .models import Type, Category, Element
from django.utils.text import slugify



class ElementForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255,  validators=[MinLengthValidator(3, message='Very short! (min %(limit_value)d) (current %(show_value)d)')])
    slug = forms.SlugField(label='Slug', max_length=255, min_length=3)
    description = forms.CharField(label='Description', initial='Content initial', widget=forms.Textarea)
    price = forms.DecimalField(label='Price', decimal_places=2, max_digits=5, required=True)
    type = forms.ModelChoiceField(label='Type', queryset=Type.objects.all(), initial=1)
    category = forms.ModelChoiceField(label='Category', queryset=Category.objects.all(), initial=2)
 

 #validacion para que el titulo sea unico
    def clean_title(self):
        title = self.cleaned_data['title']
        if Element.objects.filter(title=title).exists():
            raise ValidationError('Title already exists')
        return title


#Validacion global 
    def clean(self):
        form_data = self.cleaned_data
        if form_data['slug'] != slugify(form_data['title']):
            self._errors['slug'] = ["slug do not match with title"]
            del form_data['slug']
        return

# class ElementModelForm(forms.ModelForm):
#     class Meta:
#         model = Element
#         fields = ('title', 'slug', 'description', 'price', 'type', 'category')
