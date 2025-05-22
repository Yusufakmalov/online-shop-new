from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('store/', views.accessories, name='accessories'),
    path('search/', views.product_search, name='product_search'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>sss/', views.product_list, name='product_list_by_category'),
   
]