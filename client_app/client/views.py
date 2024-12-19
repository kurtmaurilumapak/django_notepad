from django.shortcuts import render, redirect
import requests

# Create your views here.



BASE_URL = 'http://127.0.0.1:8000/api/'  # Replace with your server IP

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        data = {'username': username, 'password': password}
        response = requests.post(f'{BASE_URL}register/', json=data)

        if response.status_code == 201:
            return redirect('login')
        else:
            return render(request, 'register.html', {'error': response.json()})

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        data = {'username': username, 'password': password}
        response = requests.post(f'{BASE_URL}token/', json=data)

        if response.status_code == 200:
            tokens = response.json()
            request.session['access_token'] = tokens['access']
            request.session['refresh_token'] = tokens['refresh']
            return redirect('home')  # Define a home view for after login
        else:
            return render(request, 'login.html', {'error': response.json()})

    return render(request, 'login.html')

from django.shortcuts import render

def home_view(request):
    if 'access_token' not in request.session:
        return redirect('login')
    return render(request, 'index.html')
