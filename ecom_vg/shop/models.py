from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    cart_id=models.CharField(max_length=250, blank=True)
    date_added=models.DateField(auto_now_add=True)
    class Meta:
        db_table='Cart'
        ordering=['date_added']
    def __str__(self):
        return '{}'.format(self.cart_id)


class CartItem(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)

