from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList, name='hub'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
]