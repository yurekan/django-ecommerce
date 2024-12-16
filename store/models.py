from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):

    name = models.CharField(max_length=200, null=True)
    price = models.JSONField(null=True, blank=True)
    highlights = models.CharField(max_length=500, null=True)
    description = models.JSONField(null=True, blank=True)  # Array of strings
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    size = models.JSONField(null=True, blank=True)
    features = models.JSONField(null=True, blank=True)  # Array of strings
    sub_category = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    specifications = models.JSONField(null=True, blank=True)  # Dictionary
    images = models.JSONField(null=True, blank=True)  # To store an array of image src links
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    review_count = models.IntegerField(null=True, blank=True)
    model = models.JSONField(null=True, blank=True)  # Array of strings
    combo = models.JSONField(null=True, blank=True)  # Array of strings
    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/images/placeholder.png'
        return url

    def __str__(self):
        return self.name
    

class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    

class OrderItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price[0] * self.quantity
        return total


class ShippingAddress(models.Model):
    
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address