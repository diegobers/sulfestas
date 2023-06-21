from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'product'

def ProductSearchView(request):
  queryset_list = Product.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  context = {
    'products': queryset_list,
    'values': request.GET
  }

  return render(request, 'products/search.html', context)