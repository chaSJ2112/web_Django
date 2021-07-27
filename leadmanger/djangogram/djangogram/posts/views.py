from django.shortcuts import render

# Create your views here.
# posts app - login success
def index(request):
    return render(request, 'posts/index.html')