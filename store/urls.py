from django.urls import path
from . import views

urlpatterns = [
    path('api/product/', views.ProductList.as_view()),
]