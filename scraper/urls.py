"""scraper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.db import router
from django.urls import path, include
from judicial import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'process', views.ProcessViewSet)
router.register(r'parties_involved', views.PartiesInvolvedViewSet)
router.register(r'parties_process', views.PartiesInvolvedProcessViewSet)
router.register('judicial', views.ProcessViewSet)


urlpatterns = [
    # path('', include(scraper.urls)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # API
    path('', views.index, name='index'),
]
