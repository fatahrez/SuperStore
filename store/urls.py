from django.urls import path
from . import views
from store.views import *
from django.conf.urls import include

urlpatterns = [
    path('api/merchant/', views.MerchantList.as_view(), name='merchant'),
    path('api/merchant/merchant-id/<pk>/', views.SoloMerchant.as_view()),
    path('api/manager/', views.ManagerList.as_view(), name='manger'),
    path('api/manager/manager-id/<int:pk>/', views.SoloManager.as_view()),
    path('api/clerk/', views.ClerkList.as_view()),
    path('api/clerk/clerk-id/<int:pk>/', views.SoloClerk.as_view()),
    path('api/product-batch/', views.ProductBatchList.as_view()),
    path('api/product-batch/<int:pk>/', ProductBatchDetail.as_view(), name='shops'),
    path('auth/', include('djoser.urls')),
    path('auth/token/login', include('djoser.urls.authtoken'), name='login'),
    path('api/shop/', ShopsList.as_view(), name='shops'),
]