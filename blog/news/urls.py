from django.urls import path
from . import views
from .views import SearchView

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('tags/', views.tags_list, name='tags_list'),
    path('search/', SearchView.as_view(), name='search_view'),
    path('detail/<int:pk>', views.news_detail, name='news_detail'),

]
