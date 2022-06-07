from django.http import Http404, HttpResponse
from django.shortcuts import render
from AppCarolina.models import Carrera, Profesor, Estudiante
from django.template import loader
from AppCarolina.forms import CarreraFormulario
from AppCarolina.forms import ProfesorFormulario
from AppCarolina.forms import EstudianteFormulario



def carrera(self):
    carrera = Carrera(nombre="Desarrollo Web", comision=31075)
    carrera.save()
    documento = f"Curso: {carrera.nombre} ..... Camada: {carrera.comision}"
    return HttpResponse(documento)


def profesores(request):
    return render(request, 'AppCarolina/profesores.html')

def carreras(request):
    return render(request, 'AppCarolina/carreras.html')

def estudiantes(request):
    return render(request, 'AppCarolina/estudiantes.html')

def inicio(self):
    plantilla = loader.get_template('AppCarolina/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def carreraFormulario(request):
    if request.method == 'POST':
        miFormulario = CarreraFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = request.POST['carrera']
            comision = request.POST['comision']
            carrera = Carrera(nombre=nombre, comision=comision)
            carrera.save()
            return render(request, "AppCarolina/inicio.html")
    else:
        miFormulario = CarreraFormulario()
    return render(request, "AppCarolina/carreraFormulario.html", {"miFormulario":miFormulario})


def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "AppCarolina/inicio.html")
            
    else:
        miFormulario = ProfesorFormulario()
    return render(request, "AppCarolina/profesorFormulario.html", {"miFormulario":miFormulario})


def estudianteFormulario(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render(request, "AppCarolina/inicio.html")
            
    else:
        miFormulario = EstudianteFormulario()
    return render(request, "AppCarolina/estudianteFormulario.html", {"miFormulario":miFormulario})


def busquedaComision(request):
    return render(request, "AppCarolina/busquedaComision.html")


def buscar(request):
        if request.GET['comision']:
            comision = request.GET['comision']
            carreras = Carrera.objects.filter(comision=comision)
            return render(request, "AppCarolina/resultadosBusqueda.html", {"carreras":carreras, "comision":comision})


        else:
            respuesta = "No se ha ingresado ninguna comisión."
        return HttpResponse(respuesta)
