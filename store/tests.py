from django.test import TestCase
from .models import Merchant, Manager, Shop, Clerk, Supplier, Item, ProductBatch, ProductSales
from django.contrib.auth.models import User

# Create your tests here.
class MerchantTest(TestCase):
    '''
    Class that tests the merchants
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.brenda = User(username="brenda", email="brenda@gmail.com", password = "12345")
        self.brenda.save()

        self.new_merchant = Merchant(first_name="Brenda", last_name="Mwangi", profile=self.brenda)
        self.new_merchant.save_merchant()


    def tearDown(self):
        '''
        Clears database after each test
        '''
        Merchant.objects.all().delete()

    
    def test_merchant_instance(self):
        '''
        Tests whether the new merchant created is an instance of  class
        '''
        self.assertTrue(isinstance(self.new_merchant, Merchant))

    
    def test_save_merchant(self):
        '''
        This tests whether new merchant is added to the db 
        '''
        self.new_merchant.save_merchant()
        merchants = Merchant.objects.all()
        self.assertTrue(len(merchants)> 0)


    def test_delete_merchant(self):
        '''
        This tests whether merchant is deleted
        '''
        self.new_merchant.save_merchant()
        merchant1 = Merchant.objects.all()
        self.assertEqual(len(merchant1),1)
        self.new_merchant.delete_merchant()
        merchant2 = Merchant.objects.all()
        self.assertEqual(len(merchant2),0)



class Manager(TestCase):
    '''
    Class that tests the manager
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.brian = User(username="brian", email="brian@gmail.com", password = "12345")
        self.brian.save()

        self.new_manager = Manager(first_name="Brian", last_name="Nabiswa", profile=self.brian)
        self.new_manager.save_manager()


    def tearDown(self):
        '''
        Clears database after each test
        '''
        Manager.objects.all().delete()

    
    def test_manager_instance(self):
        '''
        Tests whether the new manager created is an instance of  class
        '''
        self.assertTrue(isinstance(self.new_manager, Manager))

    
    def test_save_manager(self):
        '''
        This tests whether new manager is added to the db 
        '''
        self.new_manager.save_manager()
        managers = Manager.objects.all()
        self.assertTrue(len(managers)> 0)


    def test_delete_manager(self):
        '''
        This tests whether manager is deleted
        '''
        self.new_manager.save_manager()
        manager1 = Manager.objects.all()
        self.assertEqual(len(manager1),1)
        self.new_manager.delete_manager()
        manager2 = Manager.objects.all()
        self.assertEqual(len(manager2),0)



    
class Clerk(TestCase):
    '''
    Class that tests the clerks
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.jerome = User(username="jerome", email="jerome@gmail.com", password = "12345")
        self.jerome.save()

        self.new_clerk = Manager(first_name="Jerome", last_name="Mberia", profile=self.jerome)
        self.new_clerk.save_clerk()


    def tearDown(self):
        '''
        Clears database after each test
        '''
        Clerk.objects.all().delete()

    
    def test_clerk_instance(self):
        '''
        Tests whether the new clerk created is an instance of  class
        '''
        self.assertTrue(isinstance(self.new_clerk, Clerk))

    
    def test_save_clerk(self):
        '''
        This tests whether new clerk is added to the db 
        '''
        self.new_clerk.save_clerk()
        clerks = Clerk.objects.all()
        self.assertTrue(len(clerks)> 0)


    def test_delete_clerk(self):
        '''
        This tests whether clerk is deleted
        '''
        self.new_clerk.save_clerk()
        clerk1 = Clerk.objects.all()
        self.assertEqual(len(clerk1),1)
        self.new_clerk.delete_clerk()
        clerk2 = Clerk.objects.all()
        self.assertEqual(len(clerk2),0)

   
class ProductBatch(TestCase):
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.jerome = User(username="jerome", email="jerome@gmail.com", password = "12345")
        self.new_clerk = Manager(first_name="Jerome", last_name="Mberia", profile=self.jerome)

        self.supplier = Supplier(supplier_name="Anto",supplier_contact="anto@gmail.com")

        self.item = Item(item_name="Pens")

        self.new_product = ProductBatch(item=self.item, quantity=2, buying_price=100, damaged_items=20, supplier=self.supplier, clerk=self.clerk, payment_status=True)

        self.new_product.save()


    def test_get_stock_by_store(self):
        '''
        This tests whether  stock can be retrieved by store
        '''
        self.new_product.save()
        shop_sales = ProductBatch.get_stock_by_store(self.new_clerk)
        self.assertEqual(len(shop_sales),1 )
    
    def test_get_stock_by_supplier(self):
        '''
        This tests whether stock can be retrieved by supplier
        '''
        self.new_product.save()
        stock_supplier = ProductBatch.get__stock_by_supplier(self.supplier)
        self.assertEqual(len(stock_supplier),1 )
    
    def test_get_stock_by_item(self):
        '''
        This tests whether stock can be retrieved by item
        '''
        self.new_product.save()
        stock_item = ProductBatch.get_stock_by_item(self.item)
        self.assertEqual(len(stock_item),1 )


class ProductSales(TestCase):
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.brian = User(username="brian", email="brian@gmail.com", password = "12345")
        self.new_manager = Manager(first_name="Brian", last_name="Nabiswa", profile=self.brian)

        self.shop = Shop(shop_name="Tuskys", manager=self.manager)

        self.item = Item(item_name="Pens")
      
        self.product_sale = ProductSales(product=self.item , quantity=2, selling_price=2, shop=self.shop)


    def test_get_sales_by_item(self):
        '''
        This tests whether sale can be retrieved by item
        '''
        self.product_sale.save()
        item_sale = ProductSales.get_sales_by_item(self.item)
        self.assertEqual(len(item_sale),1 )
    
    def test_get_sales_by_shop(self):
        '''
        This tests whether sale can be retrieved by shop
        '''
        self.product_sale.save()
        shop_sale =ProductSales.get_sales_by_shop(self.shop)
        self.assertEqual(len(shop_sale),1 )
 

