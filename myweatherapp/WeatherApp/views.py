from datetime import datetime
import json

import requests   #pipenv install requets
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import City,Authentication
from .forms import CityForm,AuthenticationForm
import urllib.request
from IPython.display import Image, display
from . import forms

def home(request):
    if 'term' in request.GET:
        cities = City.objects.filter(name__istartswith=request.GET.get("term"))
        list1=[]
        for c in cities:
            list1.append(c.name)
        return JsonResponse(list1,safe=False)
    if 'location' in request.GET:
        city = request.GET.get('location')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=ce1634780a3a782d1f36fbab201bce67&units=metric"
        x = requests.get(url)
        y = x.json()
        context = {
            'c_name' : f"City_name:{y['name']}",
            'icon': y['weather'][0]['icon'],
            'country_code':f"country_code:{str(y['sys']['country'])}",
            'Temperature': f"Temperature: {str(y['main']['temp'])}  °C",
            'Pressure': f"Pressure: {str(y['main']['pressure'])}",
            'Humidity': f"Humidity: {y['main']['humidity']}",
            'Weather_condition': f"Weather_Condition: {y['weather'][0]['description'].upper()}"
    
        }

        return render(request, 'weatherapp.html', context)
    return render(request, 'weatherapp.html')

def register(request):
 
        saverecord = Authentication()
        if request.method =='POST':
         if request.POST.get('username') and request.POST.get('email') and request.POST.get('password') and request.POST.get('phonenumber') :
            saverecord.username=request.POST.get('username')
            saverecord.email=request.POST.get('email')
            saverecord.password=request.POST.get('password')
            saverecord.phonenumber=request.POST.get('phonenumber')
            saverecord.save()
            messages.success(request, "Registration successful." )
            return redirect("/Login")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            return render(request,'register.html')
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/Login")
#         else:
#          form = UserCreationForm()
#     return render(request,'register.html',{'form':form})



def loginview(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect('/weatherapp')
        else:
            context["error"] = "provide vaild credentials !!"
            return render(request,"login.html",context)
    else:
        return render(request,'login.html',context)

def success(request):
    context = {}
    context['user'] = request.user
    return render(request,"success.html",context)

def logout(request):
    if request.method == "POST":
        logout(request)
        return render(request,'login.html')

    # if request.method == "POST":
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = authenticate(request, email = email, password = password)
    #     print(email)
    #     print(password)
    #     if user is not None:
    #         login(request, user)
    #         print(user)
    #         messages.success(request, f' welcome {email} !!')
    #         return redirect('/weatherapp')
    #     else:
    #         messages.info(request, f'account done not exit plz sign in')
   
    # return render(request,'login.html')



# using urlib api
    #  if request.method == 'POST':
    #     city = request.POST['city']
    #     # source contain JSON data from API
    #     source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=ce1634780a3a782d1f36fbab201bce67').read()
    #     current_time = datetime.now()
    #     formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
    #     # converting JSON data to a dictionary
    #     list_of_data = json.loads(source)

    #     # data for variable list_of_data
    #     data = {
    #         'city': city,
    #         'icon': list_of_data['weather'][0]['icon'],
    #         "country_code": str(list_of_data['sys']['country']),
    #         "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
    #         "temp": str(list_of_data['main']['temp']) + 'k',
    #         "pressure": str(list_of_data['main']['pressure']),
    #         "humidity": str(list_of_data['main']['humidity']),
    #         'time': formatted_time
    #     }
    #     print(data)
    #  else:
    #     data ={}
    #  return render(request, "weatherapp.html", data)

# using request api
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ce1634780a3a782d1f36fbab201bce67'
    # cities = City.objects.all()
    # # city = 'Las Vegas'
    # # city_weather = requests.get(url.format(city)).json()
    # if request.method == 'POST':  # only true if form is submitted
    #     form = CityForm(request.POST)  # add actual request data to form for processing
    #     form.save()  # will validate and save if validate
    # form = CityForm()
    # weather_data = []
    # for city in cities:
    #     response = requests.get(url.format(city))
    #     if response.status_code == 404:
    #         continue
    #     city_weather = response.json()
    #     current_time = datetime.now()
    #     formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
    #     weather = {

    #         'city': city,
    #         'description': city_weather['weather'][0]['description'],
    #         'icon': city_weather['weather'][0]['icon'],
    #         'temperature': 'Temperature: ' + str(city_weather['main']['temp']) + ' °C',
    #         'country_code': city_weather['sys']['country'],
    #         'wind': 'Wind: ' + str(city_weather['wind']['speed']) + 'km/h',
    #         'humidity': 'Humidity: ' + str(city_weather['main']['humidity']) + '%',
    #         'time': formatted_time
    # }
    # weather_data.append(weather)
    # context = {'weather_data' : weather_data, 'form' : form}
    # return render(request, "weatherapp.html", context)
   


    
      
                   
                
          

              
