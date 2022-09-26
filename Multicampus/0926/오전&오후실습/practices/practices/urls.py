"""practices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import django0926.views
import django0926_after.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", django0926.views.index),
    path("ping/", django0926.views.ping),
    path("pong/", django0926.views.pong),
    path("", django0926_after.views.index),
    path("number/<int:_number>", django0926_after.views.print_number),
    path("print-text/", django0926_after.views.print_text),
]
