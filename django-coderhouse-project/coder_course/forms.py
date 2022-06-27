from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class cargarFamilia(forms.Form):
    codigo= forms.CharField()
    nombre=forms.CharField()
    label = "Familia"
   


class cargarRubro(forms.Form):
    codigo= forms.CharField()
    nombre=forms.CharField()
    label = "Rubros"
      
class cargarTarea(forms.Form):
    codigo = forms.CharField()
    rubro = forms.CharField()
    tarea = forms.CharField()
    unidad = forms.CharField()
    costo = forms.IntegerField()
    fecha = forms.DateField()
    especificacion = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la contraseña",widget=forms.PasswordInput)
    last_name= forms.CharField()
    first_name=forms.CharField()
    
    

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2","last_name", "first_name"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()