"""
URL configuration for dmsproject project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('checkadminlogin',views.checkadminlogin,name='checkadminlogin'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('orgsignup',views.orgsignup,name='orgsignup'),
    path('orgsignedup',views.orgsignedup,name='orgsignedup'),
    path('donorsignup',views.donorsignup,name='donorsignup'),
    path('donorsignedup',views.donorsignedup,name='donorsignedup'),
    path('',include("adminapp.urls")),
    path('',include('donorapp.urls')),
    path('',include('orgapp.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
