"""
    website URL Configuration

"""

from django.urls import include, path
from django.contrib import admin
from documents import views

urlpatterns = [
    path('documents/', include('documents.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
