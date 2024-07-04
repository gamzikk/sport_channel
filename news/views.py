from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


def news(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})


def get_sport_new(request, new_id):
    new = Articles.objects.get(pk = new_id)
    comments = Comment.objects.filter(article=new)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = new
            comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'news/new.html', {'new': new, 'comments': comments, 'comment_form': comment_form})


def search(request):
    results = []

    if request.method == "GET":
        query = request.GET.get('search')

        if query == '':
            query = 'ghgjghf'
    results = Articles.objects.filter(Q(title__icontains=query))

    return render(request, 'main/search.html', {'query': query, 'results': results})