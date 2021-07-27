from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import SignUpForm

# users app - login 
def main(request):
    if request.method == 'GET':
        return render(request, 'users/main.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('posts:index'))
        else:
            return render(request, 'users/main.html')        

def signup(request):
    # 화면 요청 GET
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})
    
    # 회원가입 요청 POST
    elif request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid:
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('posts:index'))
            
        return render(request, 'users/main.html')
