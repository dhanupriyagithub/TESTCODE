from django.forms import ModelForm, TextInput,fields,Widget
from .models import City,Authentication


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets={'name': TextInput(attrs={'class':'input','placeholder':'CityName','id':'cities'})}

class AuthenticationForm(ModelForm):  
    class Meta:  
        model = Authentication  
        fields = "__all__"  