from django.shortcuts import redirect, render
from django.http import request
from .forms import ElementForm #, ElementModelForm
from .models import Element
from django.core.paginator import Paginator

# Create your views here.
def add(request):
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            element = Element()
            element.title = form.cleaned_data['title']
            element.slug = form.cleaned_data['slug']
            element.description = form.cleaned_data['description']
           #element.price = form.cleaned_data['price']
            element.category = form.cleaned_data['category']
            element.type = form.cleaned_data['type']
            element.save()
        return redirect('element:index')
    else:
        form = ElementForm()
    
    return render(request, 'element/add.html', {'form': form})



# def add2(request):
#     if request.method == 'POST':
#         form = ElementModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = ElementModelForm()
    
#     return render(request, 'element/add.html', {'form': form})



def index(request):
    elements = Element.objects.all()
    paginator = Paginator(elements, 10)

    page_number = request.GET.get('page')
    return render(request, 'element/index.html', {'elements': paginator.get_page(page_number)})