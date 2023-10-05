from django.urls import path 
from . import views

urlpatterns=[
    path('product/<int:product_id>/', views.product, name="product"),
    path('products/', views.products, name="products"),
    path('cart/', views.cart, name='cart'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    ]








