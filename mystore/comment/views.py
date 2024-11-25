from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Comment
from .forms import CommentForm
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.


def list_comment(request):
    comment = Comment.objects.all()

    return render(request, 'list_comment.html', {'comment': comment})


#CRUD COMMENTS
def index(request):
    comments = Comment.objects.all()
    #comments = get_list_or_404(Comment, pk__gt=14)
    paginator = Paginator(comments, 10)
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)

    return render(request, 'index.html',{'comments': comments_page})



def update_comment(request, pk):

    comment = get_object_or_404(Comment, pk=pk)
    # try:
    #     comment = Comment.objects.get(pk=pk)

    # except Comment.DoesNotExist:
    #     raise Http404
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'add.html', {'form': form})



def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('/')
   
    
# def add(request):
#      if (request.method == 'GET'):
#          pass
#      if (request.method == 'POST'):
#          if request.POST.get('text') != '':
#              comment = Comment()
#              comment.text = request.POST.get('text')
#              comment.save()
#          else:
#              print('Campo vacio')
#      return render(request, 'add.html')


def add(request):
    if (request.method == 'POST'):
        form = CommentForm(request.POST)
        form.save()
        return redirect('/')
    else:
        form = CommentForm()
    return render(request, 'add.html', {'form': form})