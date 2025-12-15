from django.urls import path
from . import views

urlpatterns = [
    path('', views.smoothie_list, name='smoothie_list'),
]
