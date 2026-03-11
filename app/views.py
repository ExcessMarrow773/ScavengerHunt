from django.shortcuts import render

from .models import request as Request

# Create your views here.

def index(request):
	context = {
	}
	return render(request, 'index.html', context)

def requests(request):
	requests = Request.objects.all()
	context = {
		'requests': requests
	}
	return render(request, 'requests.html', context)