from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import Note
import requests

BASE_URL = 'http://127.0.0.1:8000/api/'  # Replace with your server's API endpoint

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        data = {'username': username, 'password': password}
        try:
            response = requests.post(f'{BASE_URL}register/', json=data)
            if response.status_code == 201:
                return redirect('login')
            else:
                error_message = response.json().get('error', 'Registration failed.')
                return render(request, 'register.html', {'error': error_message})
        except requests.exceptions.RequestException:
            return render(request, 'register.html', {'error': 'Server unavailable. Try again later.'})
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # Invalid login attempt
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

@login_required
def home_view(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'index.html', {'notes': notes})


def logout_view(request):
    request.session.flush()
    return redirect('login')

@login_required
@csrf_protect
def add_note_view(request):
    if request.method == 'POST':
        note_content = request.POST.get('note_content')
        if note_content:
            try:
                Note.objects.create(notes=note_content, user=request.user)  # Use 'notes' field
                return redirect('home')
            except Exception as e:
                print(f"Error while saving note: {e}")
                return render(request, 'index.html', {'error': 'Failed to save note.'})
    notes = Note.objects.filter(user=request.user)
    return render(request, 'index.html', {'notes': notes})
