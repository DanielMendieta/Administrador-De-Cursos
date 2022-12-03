from django.urls import path
from Aplicaciones.Academia.views import Cursolistview, registrar_curso, eliminar_curso, edicion_curso, editar_curso, contacto

urlpatterns = [
    path ('',Cursolistview.as_view(), name = 'Academia'),
    path ('registrarCurso/', registrar_curso),
    path ('eliminarCurso/<int:id>', eliminar_curso ),
    path ('edicionCurso/<int:id>', edicion_curso),
    path ('editarCurso/', editar_curso),
    path ('contacto/', contacto)
]