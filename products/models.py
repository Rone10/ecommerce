from django.db import models
from django.urls import reverse
CATEGORIES = (
    ('sh', 'Shoes'),
    ('Ha', 'Hats'),
    ('P', 'Pants')
)
class Product(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(upload_to='products', default='products/shoe.jpg')
    price = models.DecimalField(decimal_places=2, max_digits=7)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    description = models.TextField()
    slug = models.SlugField(max_length=100)
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('account:detail', kwargs={ 'pk': self.pk })



