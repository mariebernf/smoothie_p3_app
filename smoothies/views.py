from django.shortcuts import render

def home(request):
    return render(request, 'smoothies/home.html')

def css_test(request):
    return render(request, 'smoothies/base.html')
