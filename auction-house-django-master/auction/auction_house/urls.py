from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('post_new',views.post_new,name="post_new"),
    path('products/',views.ProductListView.as_view(),name="products"),
    path('products/<int:pk>/',views.ProductDetailView.as_view(),name="product-detail")
]