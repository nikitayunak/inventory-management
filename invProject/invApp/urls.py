from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/create/', views.product_create_view, name='product_create'),
    path('products/', views.product_list_view, name='product_list'),
    path('products/update/<int:product_id>/', views.product_update_view, name='product_update'),
    path('products/delete/<int:product_id>/', views.product_delete_view, name='product_delete'),
]