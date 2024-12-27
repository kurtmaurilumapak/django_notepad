from django.shortcuts import render, redirect
import requests

# Create your views here.



BASE_URL = 'http://127.0.0.1:8000/api/'  # Replace with your Host IP

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

def home_view(request):
    if 'access_token' not in request.session:
        return redirect('login')

    # Get the access token from the session
    access_token = request.session['access_token']

    # Fetch user data from the server
    headers = {
        'Authorization': f'Bearer {access_token}',  # Include the token in the request
    }

    try:
        response = requests.get(f'{BASE_URL}user-data/', headers=headers)
        if response.status_code == 200:
            user_data = response.json()  # Parse the user data
        else:
            user_data = {'error': 'Failed to fetch user data'}
    except Exception as e:
        user_data = {'error': str(e)}

    return render(request, 'index.html', {'user_data': user_data})



def logout_view(request):
    if request.method == 'POST':
        # Clear session data
        request.session.flush()
        # Redirect to login page
        return redirect('login')
    return redirect('home')  # Redirect to home if accessed via GET