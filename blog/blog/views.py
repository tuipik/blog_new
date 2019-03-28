from django.http import HttpResponse
from  django.shortcuts import redirect

def blog_redirect(request):
    return redirect(news_list, permanent=True)
