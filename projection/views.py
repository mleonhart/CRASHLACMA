from django.shortcuts import render

def projection_home(request):
    return render(request, "projection/projection_home.html")