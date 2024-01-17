"""
URL configuration for ad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import adserver.views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', adserver.views.index),
    path('add_product/', adserver.views.add_product, name='add_product'),
    path('add_ad/', adserver.views.add_ad, name='add_ad'),
    path('search_ad/', adserver.views.search_ad, name="search_ad"),
    path('detail_ad/', adserver.views.detail_ad, name="detail_ad"),
    path('modify_ad/', adserver.views.modify_ad, name="modify_ad"),
    path('delete_ad/', adserver.views.delete_ad, name="delete_ad"),
    path('test_ad/', adserver.views.test_ad, name="test_ad"),
    
]
