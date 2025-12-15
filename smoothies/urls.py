from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('css_test/', views.css_test, name='css_test'),
]
