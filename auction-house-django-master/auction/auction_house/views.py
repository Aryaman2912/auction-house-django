from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'auction_house/home.html')

