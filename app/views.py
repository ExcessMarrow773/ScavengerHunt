from django.shortcuts import render

from .models import request as Request

# Create your views here.

def index(request):
	requests = Request.objects.all()
	context = {
		'requests': requests
	}
	return render(request, 'index.html', context)