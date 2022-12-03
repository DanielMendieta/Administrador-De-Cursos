from django.shortcuts import render,redirect
from .models import cursos
from django.views.generic import ListView

# Create your views here.


"""
def home(request):
    cursoslistados=cursos.objects.all() .order_by('nombre')#Con order by hacemos que se acomoden alfabeticamente
    data = {
            'titulo': 'Academia',
            'cursos': cursoslistados}
    return render (request, "plantilla.html", data)
"""

class Cursolistview(ListView):    
    model= cursos 
    template_name= 'plantilla.html'

    def get_queryset(self):
        return cursos.objects.all() .order_by('nombre')

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Academia'
        return context

def registrar_curso(request):
    nombre=request.POST['txtNombre']
    creditos=request.POST['CreditosDelCurso']
    curso = cursos.objects.create(nombre=nombre, creditos=creditos)
    return redirect('/')


def eliminar_curso(request,id):
    curso = cursos.objects.get (id=id)
    curso.delete()
    return redirect('/')

def edicion_curso(request, id):
    curso = cursos.objects.get (id=id)
    data = {
            'titulo': 'Edicion de Curso',
            'curso': curso
}    
    return render (request, "edicionCurso.html", data)


def editar_curso(request):
    id = int (request.POST['id'])
    nombre = request.POST['txtNombre']
    creditos = request.POST ['CreditosDelCurso'] 

    curso = cursos.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    return redirect('/')  

def contacto (request):
    return render(request, "contacto.html")

