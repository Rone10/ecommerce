from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(upload_to='products', default='')
    price = models.DecimalField()
    category = models.CharField(max_length=100, choices='')
    description = models.TextField()
    slug = models.SlugField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('account:detail', kwargs={ 'pk': self.pk })



