"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from genres.views import ListCreateView, detail, update, delete


urlpatterns = [
    path("admin/", admin.site.urls),
    path("genres/create", ListCreateView.as_view(), name="genre-create"),
    path("genres/update/<int:pk>", update, name="genre-update"),
    path("genres/delete/<int:pk>", delete, name="genre-delete"),
    path("genres/detail/<int:pk>/", detail, name="genre-detail"),
    path("genres/list", ListCreateView.as_view(), name="genre-list"),
]
