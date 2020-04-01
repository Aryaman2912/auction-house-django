from django.shortcuts import render,HttpResponse
from .forms import ProductForm

# Create your views here.

def home(request):
    return render(request,'auction_house/home.html')

def post_new(request):
    form = ProductForm()
    return render(request,'auction_house/post_new.html',{'form':form})

