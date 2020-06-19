from django.urls import path
from . import views
from store.views import *

urlpatterns = [
    path('api/merchant/', views.MerchantList.as_view(), name='merchant'),
    path('api/merchant/merchant-id/<pk>/', views.SoloMerchant.as_view()),
    path('api/manager/', views.ManagerList.as_view(), name='manger'),
    path('api/manager/manager-id/<pk>/', views.SoloManager.as_view()),
    path('api/product-batch/', views.ProductBatchList.as_view()),
    path('api/product-batch/<int:pk>/', ProductBatchDetail.as_view(), name='shops'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('api/shop/', ShopsList.as_view(), name='shops'),

]