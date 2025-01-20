from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import RegisterForm, LoginForm
from .models import User

# Create your views here.
def home (request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.authenticate()
            if user is not None:
                auth_login(request, user)
                # Redirect based on role
                if user.role == 'admin':
                    return redirect('dashboard')  # Admin role goes to dashboard
                elif user.role == 'Farmer':
                    return redirect('home')  # Farmer role goes to index
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')


#---------------------------------------------------------------------

import requests
from django.http import JsonResponse

def get_weather(request):
    api_key = 'be3b88f1ba1a1a5af46b6dd38ea6b1e2'  # ใส่ API Key จาก OpenWeatherMap
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lon')

    if not latitude or not longitude:
        return JsonResponse({'error': 'Latitude and longitude are required.'}, status=400)

    # เรียก API ของ OpenWeatherMap
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        # ตรวจสอบและดึงข้อมูล
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        rainfall = weather_data.get('rain', {}).get('1h', 0)  # ปริมาณฝนใน 1 ชั่วโมง (ถ้ามี)

        return JsonResponse({
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'rainfall': rainfall
        })
    else:
        return JsonResponse({'error': 'Unable to fetch weather data.'}, status=response.status_code)

