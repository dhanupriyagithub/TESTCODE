from django.contrib import admin
from django.urls import path
from django.conf import settings
from WeatherApp import views

from django.views.static import serve
from django.conf import url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("weatherapp",views.home,name="Home"),
    path("Login/",views.loginview,name="Login"),
    path("Register/",views.register,name="Register"),
    path("success/",views.success,name="success"),
    path("",views.logout,name="Logout"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

