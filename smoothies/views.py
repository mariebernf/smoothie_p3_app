from django.shortcuts import render

def home(request):
    return render(request, 'smoothies/smoothie_list.html')
