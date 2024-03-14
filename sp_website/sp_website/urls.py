"""
URL configuration for sp_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.staticfiles.views import serve
from login import views as login_views
from index import views as index_views

def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_views.login, name='login'),
    path("signup/", login_views.signup, name='signup'),
    path("index/", index_views.index, name='index'),
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    path('success/', login_views.success, name='success'),
]
