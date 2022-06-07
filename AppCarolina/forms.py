from django import forms

class CarreraFormulario(forms.Form):

    
    carrera = forms.CharField(max_length=50)
    comision = forms.IntegerField()

class ProfesorFormulario(forms.Form):

    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    
    
