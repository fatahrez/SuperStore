from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Merchant(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.username

    @receiver(post_save, sender = User)
    def create_merchant(sender, instance,created, **kwargs):
        if created:
            Merchant.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_merchant( sender, instance, **kwargs):
        instance.profile.save()

class Manager(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.username

class Shop(models.Model):
    shop_name = models.CharField(max_length=50, null=True)
    manger = models.OneToOneField(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name

class Clerk(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.profile.username
    
class Product(models.Model):
    product_name = models.CharField(max_length=50, null=True)
    buying_price = models.IntegerField(null=True)
    selling_price = models.IntegerField(null=True)
    date_purchased = models.IntegerField(null=True)
    paid_for = models.BooleanField(default=False)
    good_condition = models.BooleanField(default=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    # counting products that are spoilt
    # @classmethod
    # def number_of_spoilt_products(cls):
    #     spoilt = Product.objects.filter(good_condition=False).count()
    #     return spoilt

    # counting number of product in the stock
    # @classmethod
    # def number_of_products(cls):
    #     n_products = Product.objects.all().count()
    #     return n_products
    
    # counting product that 

