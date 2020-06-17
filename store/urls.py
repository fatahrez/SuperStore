from django.urls import path
from . import views

urlpatterns = [
    path('api/product/', views.ProductBunchList.as_view()),
]