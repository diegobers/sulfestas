from django.db import models
from datetime import datetime


class Product(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  photo_main = models.ImageField(upload_to='img/product')
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
    
  def __str__(self):
    return self.title