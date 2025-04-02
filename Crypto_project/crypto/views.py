from django.shortcuts import render, redirect
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import User
from .forms import UserForm, MyUserCreationForm
from .ml_model import predict_price



def predict_view(request):
    prediction = None
    crypto_name = "bitcoin"
    if request.method == "POST":
        crypto_name = request.POST.get("crypto", "bitcoin").lower()
        try:
            prediction = predict_price(crypto_name)
        except Exception as e:
            prediction = {"Error": str(e)}
    return render(request, "crypto/predictions.html", {"prediction": prediction, "crypto_name": crypto_name})



def home(request):
    return render(request, 'crypto/dashboard.html')


def future(request):
    return render(request, 'crypto/predictions.html')



def about(request):
    return render(request, 'crypto/about.html')




def contacts(request):
    return render(request, 'crypto/contacts.html')



def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
            return redirect('login')
            
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')
            
        
    context = {'page': page}
    return render(request, 'crypto/login_register.html', context)



def logoutUser(request):
    logout(request)
    return redirect('home')



def registerPage(request):
    page = 'register'
    form = MyUserCreationForm()
    
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()   
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Ann error occured during registration")
        
    return render(request, 'crypto/login_register.html', {'form': form})






@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')    
    return render(request, 'crypto/update-user.html', {'form':form})





def bot_page(request):
    bot_username = "Crypt0_UA_Bot"
    return render(request, "crypto/services.html", {"bot_username": bot_username})
