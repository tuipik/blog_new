from django.urls import path
from . import views
from .views import SearchView

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('tag/<int:pk>/', views.tag_detail, name='tag_detail'),
    path('tags/', views.tags_list, name='tags_list'),
    path('categories/', views.categories_list, name='categories_list'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('search/', SearchView.as_view(), name='search_view'),
    path('detail/<int:pk>', views.news_detail, name='news_detail'),

]
