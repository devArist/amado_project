from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('product', views.product, name='product'),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path(
        'product/category/<str:name>', 
        views.product_category, 
        name='product-category'
        ),
    path('product/news',views.news, name='news')
]
