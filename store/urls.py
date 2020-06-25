from django.urls import path
from . import views

urlpatterns = [
    path('register-merchant', views.MerchantRegistration.as_view()),
    path('register-manager', views.ManagerRegistration.as_view()),
    path('register-clerk', views.ClerkRegistration.as_view()),
    path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(),name='activate'),
    path('login', views.UserLogin.as_view(),name='login'),
    path('api/merchant/', views.MerchantList.as_view()),
    path('api/manager/', views.ManagerList.as_view()),
    path('api/clerk/', views.ClerkList.as_view()),
    path('api/merchant/merchant-id/<pk>/', views.SoloMerchant.as_view()),
    path('api/manager/manager-id/<pk>/', views.SoloManager.as_view()),
    path('api/clerk/clerk-id/<pk>/', views.SoloClerk.as_view()),
    path('api/items/', views.ItemList.as_view()),
    path('api/purchases/', views.PurchaseList.as_view()),
    path('api/sales/', views.SalesList.as_view()),
   
]