import code
from django.shortcuts import render
from datetime import datetime
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from coder_course.forms import cargarFamilia, cargarRubro, cargarTarea, UserRegisterForm, UserEditForm, AvatarFormulario
from coder_course.models import Familias, Insumos, Rubros, Tareas, Avatar
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import string

# Create your views here.


def index2(request):
    return render(request, "coder_course/index.html")

@login_required
def insumos(request):
    return render(request, "coder_course/insumos.html")

def tareas(request):
    if request.method == "POST":
        miFormulario = cargarTarea(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            tarea = Tareas(codigo=informacion["codigo"],rubro=informacion["rubro"],tarea=informacion["tarea"],unidad=informacion["unidad"],costo=informacion["costo"],fecha=informacion["fecha"],especificacion=informacion["especificacion"])
            tarea.save()

            
            return render (request,"coder_course/index.html")
                 
    else:
        miFormulario=cargarTarea()
    return render (request,"coder_course/tareas.html",{"miFormulario":miFormulario})

def rubros(request):
    if request.method == "POST":
        miFormulario = cargarRubro(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            rubro = Rubros(codigo=informacion["codigo"],nombre=informacion["nombre"])
            rubro.save()

            
            return render (request,"coder_course/index.html")
                 
    else:
        miFormulario=cargarRubro()
    return render (request,"coder_course/rubros.html",{"miFormulario":miFormulario})

#def familias(request):
    return render(request, "coder_course/familias.html" )

def iniciar(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        context_dict = {"url":avatars[0].avatares.url}
    else:
        context_dict={}
    return render (
        request=request,
        context=context_dict,
        template_name="coder_course/iniciar.html")

def familias(request):
    if request.method == "POST":
        miFormulario = cargarFamilia(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            KEY_LEN = 20
            name_list = [random.choice((string.ascii_letters + string.digits)) for _ in range (KEY_LEN)]
            mock_name = ''.join(name_list)

            print(f'----> Prueba con: {mock_name}')

            familia = Familias(codigo=informacion["codigo"],nombre=informacion["nombre"])
            familia.save()

            
            return render (request,"coder_course/index.html")
                 
    else:
        miFormulario=cargarFamilia()
    return render (request,"coder_course/familias.html",{"miFormulario":miFormulario})

def busquedaCodigo(request):
    return render(request, "coder_course/busquedaCodigo.html")

def buscar(request):
    if request.GET["codigo"]:
        codigo = request.GET['codigo']
        familia = Familias.objects.filter(codigo__icontains=codigo)
        return render(request,"coder_course/resultadosBusqueda.html", {"codigo":codigo, "familia":familia})
    else:
        respuesta = "No enviaste datos"
    return render(request, "coder_course/index.html",{"respuesta":respuesta})

def leerFamilias (request):
    familias = Familias.objects.all()
    context_dict = {
        'familias':familias
        }
    return render (
        request=request,
        context=context_dict,
        template_name="coder_course/leerFamilias.html"
    )

class FamiliasList(ListView):
    model = Familias
    template_name = "coder_course/familias_list.html"

class FamiliasDetalle(DetailView):
    model = Familias
    success_url = "coder_course/familias_detalle.html"
    

class FamiliasCreacion(CreateView):
    model = Familias
    success_url= "/coder_course/familias/list"
    fields = ['codigo','nombre']

class FamiliasUpdate(UpdateView):
    model = Familias
    success_url= "/coder_course/familias/list"
    fields = ['codigo','nombre']

class FamiliasDelete(DeleteView):
    model = Familias
    success_url= "/coder_course/familias/list"

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                
                return render(request, "coder_course/iniciar.html", {"mensaje":f"Bienvenido {usuario}" })

                
            else:
               return render(request, "coder_course/iniciar.html", {"mensaje":"Error" })

        else:
           return render(request, "coder_course/iniciar.html", {"mensaje":"Error, formulario erroneo" })

    form = AuthenticationForm()

    return render(request, "coder_course/login.html", {'form':form})


def register(request):

    if request.method == "POST":
        #form = UserCreationForm(request.post)
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "coder_course/iniciar.html", {"mensaje":"Usuario creado:)" })             

                    
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render (request, "coder_course/registro.html",{"form":form})

def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid: 
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion ['password2']
            usuario.save()

            return render(request, "coder_course/iniciar.html")

    else:
        miFormulario=UserEditForm(initial={'email':usuario.email})

    return render(request, "coder_course/editarPerfil.html",{"miFormulario":miFormulario,"usuario":{usuario}})

def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, avatares=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render(request,"coder_course/iniciar.html")
    else:
        miFormulario=AvatarFormulario()
    return render(request, "coder_course/agregarAvatar.html",{"miFormulario":miFormulario})
            