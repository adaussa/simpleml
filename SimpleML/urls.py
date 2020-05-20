"""SimpleML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    #path("register/", v.register, name="register"), 
    path('hub/', include('hub.urls')),
    path('news/', include('news.urls')),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login_user/', views.user_login, name='login_user'),
    path('logout/', views.user_logout, name='logout'),
    path('', include("django.contrib.auth.urls")),
    path('policy/', views.policy, name="policy"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
