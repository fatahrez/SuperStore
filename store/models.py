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


    def save_merchant(self):
        self.save()

    def delete_merchant(self):
        self.delete()




class Manager(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.username


    def save_manager(self):
        self.save()

    def delete_manager(self):
        self.delete()



class Shop(models.Model):
    shop_name = models.CharField(max_length=50, null=True)
    manager = models.OneToOneField(Manager, on_delete=models.CASCADE)
    #changes to manager 

    def __str__(self):
        return self.shop_name

    def save_shop(self):
        self.save()

    def delete_shop(self):
        self.delete()

    @classmethod
    def get_shop_by_manager(cls,manager):
        shop = cls.objects.filter(manager=manager)
        return shop




class Clerk(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.profile.username

    def save_clerk(self):
        self.save()

    def delete_clerk(self):
        self.delete()

    
    @classmethod
    def get_clerk_by_manager(cls,manager):
        clerks = cls.objects.filter(manager=manager).all()
        return clerks



class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50, null=True)
    supplier_contact = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.supplier_name

    def save_supplier(self):
        self.save()

    def delete_supplier(self):
        self.delete()



class Item(models.Model):
    item_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.item

    def save_item(self):
        self.save()

    def delete_item(self):
        self.delete()



class ProductBatch(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=True)                   
    buying_price = models.IntegerField(null=True)
    date_received = models.DateField(auto_now_add=True)
    damaged_items = models.IntegerField(null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    clerk = models.ForeignKey(Clerk, on_delete=models.DO_NOTHING)
    payment_status = models.BooleanField(default=False)


    def __str__(self):
        return self.stock

    def save_stock(self):
        self.save()

    def delete_stock(self):
        self.delete()

    @classmethod
    def get_stock_by_store(cls,clerk):
        store_stock = cls.objects.filter(clerk=clerk).all()
        return store_stock

    
    @classmethod
    def get_stock_by_supplier(cls,supplier):
        supplier_stock = cls.objects.filter(supplier=supplier).all()
        return supplier_stock

    @classmethod
    def get_stock_by_item(cls,item):
        supplier_stock = cls.objects.filter(item=item).all()
        return supplier_stock
        
    def batch_cost_per_item_order(self):
        total = self.quantity * self.buying_price
        return total



class ProductSales(models.Model):
    product = models.ForeignKey(Item, on_delete=models.DO_NOTHING) 
    quantity = models.IntegerField(null=True)                      
    selling_price = models.IntegerField(null=True)
    sale_date = models.DateField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.item_name

    def save_sales(self):
        self.save()

    def delete_sales(self):
        self.delete()

    @classmethod
    def get_sales_by_shop(cls,shop):
        sales = cls.objects.filter(shop=shop)
        return sales

    @classmethod
    def get_sales_by_item(cls,product):
        product_sales = cls.objects.filter(product=product).count()
        return product_sales


    def get_cost_of_sale(self):
        total = self.quantity * self.selling_price
        return total


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

