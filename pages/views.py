from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage_view(request):
	return render(request,'pages/index.html')

def about_view(request):
	return render(request,'pages/about.html')