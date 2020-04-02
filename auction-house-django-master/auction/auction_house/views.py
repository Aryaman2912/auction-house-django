from django.shortcuts import render,HttpResponse
from django.views import generic
from .forms import ProductForm
from .models import Product

# Create your views here.

def home(request):
    return render(request,'auction_house/home.html')

class ProductListView(generic.ListView):
	model = Product
	context_object_name = "product_list"				#Name of product list as a template variable
	template_name = "auction_house/product_list.html"   #Name of the template to be displayed

class ProductDetailView(generic.DetailView):
	model = Product


def post_new(request):
    form = ProductForm()
    return render(request,'auction_house/post_new.html',{'form':form})


