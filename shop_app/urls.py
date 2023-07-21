from django.urls import path, include
from . import views
app_name='shop_app'

urlpatterns = [
    path('', views.allproducts,name='allproducts'),
    path('<slug:c_slug>/',views.allproducts,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='prodetail'),
    ]
