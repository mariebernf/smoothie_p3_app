from django.shortcuts import render
from .models import Smoothie

def smoothie_list(request):
    smoothies = Smoothie.objects.all().order_by('-date_created')
    return render(
        request,
        'smoothies/smoothie_list.html',
        {'smoothies': smoothies}
    )
