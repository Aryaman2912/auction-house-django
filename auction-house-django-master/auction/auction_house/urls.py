from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('/post_new',views.post_new,name="post_new")
]