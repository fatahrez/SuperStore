from django.urls import path
from . import views

urlpatterns = [
    path('api/merchant', views.MerchantList.as_view()),
    path('api/manager', views.ManagerList.as_view()),
    path('api/clerk', views.ClerkList.as_view()),
    path('api/merchant/merchant-id/<pk>', views.SoloMerchant.as_view()),
    path('api/manager/manager-id/<pk>', views.SoloManager.as_view()),
    path('api/clerk/clerk-id/<id>', views.SoloClerk.as_view())
   
]