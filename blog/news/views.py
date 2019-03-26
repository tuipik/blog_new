from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CommentForm
from django.db.models import Q
from django.views import View

# Create your views here.


def news_list(request):

    news = News.objects.all()

    return render(request, 'news/news_list.html', {'news': news})


def tags_list(request):

    tags = Tag.objects.all()

    return render(request, 'news/tags_list.html', {'tags': tags})


# def tags_detail(request, pk):
#     tag = get_object_or_404(Tag, id=pk)
#     return render(request, 'news/tags_detail.html',
#                   {'tag': tag})


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
    template_name = 'news/search.html'

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('search', '')
        founded_news = News.objects.filter(Q(title__icontains=search_query) |
                                       Q(text__icontains=search_query))
        context = {'founded_news': founded_news}
        return render(self.request, self.template_name, context)


