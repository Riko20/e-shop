
from django.urls import path
from internet_shop import views

urlpatterns = [
    path('', views.home, name='home'),
]