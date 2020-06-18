from django.urls import path
from . import views

urlpatterns = [
    path('api/product/', views.ProductBatchList.as_view()),
]