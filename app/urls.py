from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
	path('requests/', views.requests, name="requests")
]