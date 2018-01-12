"""
    website URL Configuration

"""

from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static

from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('documents/', include('documents.urls')),
    path('admin/', admin.site.urls),
]
