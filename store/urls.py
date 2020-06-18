from django.urls import path
from . import views
from store.views import *

urlpatterns = [
    path('api/merchant', views.MerchantList.as_view()),
    path('api/manager', views.ManagerList.as_view()),
    # path('api/clerk', views.ClerkList.as_view()),
    path('api/merchant/merchant-id/<pk>', views.SoloMerchant.as_view()),
    path('api/manager/manager-id/<pk>', views.SoloManager.as_view()),
    # path('api/clerk/clerk-id/<pk>', views.SoloClerk.as_view()),
    path('api/product-batch/', views.ProductBatchList.as_view()),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]