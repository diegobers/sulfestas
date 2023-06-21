from django.urls import path

from . import views


urlpatterns = [  
  path('', views.ProductListView.as_view(), name='products'),   
  path('produto/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
  path('pesquisa', views.ProductSearchView, name='search'),
]