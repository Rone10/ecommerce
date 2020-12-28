from django.db import models
from django.urls import reverse
from django.conf import settings
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

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={ 'slug': self.slug})


class OrderProduct(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    removed_from_cart = models.BooleanField(default=False)
    
    def total(self):
        return self.quantity * self.product.price

    def product_name(self):
        return self.product.name


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def order_total(self):
        total = 0
        for prod in self.products.all():
            total += prod.total() 
        return total


   

    
