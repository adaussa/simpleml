from . import views
from django.urls import path

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:news_id>/', views.newsDetail, name='news_detail'),
]