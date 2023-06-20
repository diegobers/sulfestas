from django.urls import path

from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/index.html'), name='index'),
    #path('about', views.about, name='about'),
]
