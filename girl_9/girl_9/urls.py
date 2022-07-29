"""girl_9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from girlsmap.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', Map, name='Map'),
    path('map/search', Search, name='Search'),
    path('main/', Main, name='Main'),
    path('main/<int:bar_id>', Detail, name='Detail'),
    path('new/', New, name='New'),
    path('create/', Create, name='Create'),
    path('edit/<int:bar_id>', Edit, name='Edit'),
    path('update/<int:bar_id>', Update, name='Update'),
    path('delete/<int:bar_id>', Delete, name='Delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
