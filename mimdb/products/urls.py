from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('s/',views.search,name="search"),
    path('products/',views.all,name='products'),
    path('products/<slug:slug>',views.single_product,name='single_product'),
    
]