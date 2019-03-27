from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CommentForm
from django.db.models import Q, CharField, TextField
from django.db.models.functions import Lower
from django.views import View

# Create your views here.


def news_list(request):
    news = News.objects.filter(published=True)
    return render(request, 'news/news_list.html', {'news': news})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'news/categories_list.html', {'categories': categories})


def category_detail(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, 'news/category_detail.html', {'category': category})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'news/tags_list.html', {'tags': tags})


def tag_detail(request, pk):
    tag = Tag.objects.get(id=pk)
    return render(request, 'news/tag_detail.html', {'tag': tag})


def news_detail(request, pk):
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(news_detail, pk)
    else:

        form = CommentForm()
    return render(request, 'news/news_detail.html',
                  {'new': new, 'comments': comment, 'form': form})


class SearchView(View):
    CharField.register_lookup(Lower, "lower")
    TextField.register_lookup(Lower, "lower")
    template_name = 'news/search.html'

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('search', '')
        print(search_query.lower())

        founded_news = News.objects.filter(Q(title__lower__icontains=search_query) |
                                       Q(text__lower__icontains=search_query))
        context = {'founded_news': founded_news}
        return render(self.request, self.template_name, context)


