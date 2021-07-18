from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'gamerental/index.html')

def packages(request):
    return render(request, 'gamerental/packages.html')