from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Merchant(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='merchant_profile')

    def __str__(self):
        return self.profile.username

class Manager(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager_profile')

    def __str__(self):
        return self.profile.username

class Shop(models.Model):
    shop_name = models.CharField(max_length=50, null=True)
    manger = models.OneToOneField(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name

class Clerk(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='clerk_profile')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.profile.username

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=20, null=True)
    supplier_contant = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.supplier_name

class Item(models.Model):
    item_name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.item_name

class ProductBatch(models.Model):

    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)

    buying_price = models.IntegerField(null=True)

    date_received = models.DateField(auto_now_add=True)

    damaged_items = models.IntegerField(null=True)

    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)

    clerk = models.ForeignKey(Clerk, null=True, on_delete=models.SET_NULL)

    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.item.item_name


class ProductSales(models.Model):
    product = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=True)
    selling_price = models.DateField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.item_name

