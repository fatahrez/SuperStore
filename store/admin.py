from django.contrib import admin
from .models import *


admin.site.register(Manager)
admin.site.register(Shop)
admin.site.register(Clerk)
admin.site.register(Merchant)
admin.site.register(Product)

