"""raiek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('base.html', views.home, name='home'),
    path('accountInformation.html', views.accountInformation, name='AccInfo'),
    path('accountHistory.html', views.accountHistory, name='AccHist'),
    path('blockCount.html', views.blockCount, name='BlockCount'),
    path('nodeVersion.html', views.nodeVersion, name='nodeVersion'),
    path('representativesOnline.html', views.representativesOnline, name='RepOnline')
]