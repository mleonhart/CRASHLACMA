from django.shortcuts import render

def browse_home(request):
    return render(request, "browse/browse_home.html")