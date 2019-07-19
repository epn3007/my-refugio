from django.urls import path, include

#   RESTRINGIR LAS URL'S #
from django.contrib.auth.decorators import login_required

from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, \
	SolicitudDelete

app_name = 'adopcion' 	

urlpatterns = [
    path('index', index_adopcion),
    path('solicitud/listar', login_required(SolicitudList.as_view()), name= 'solicitud_listar' ),
    path('solicitud/nueva', login_required(SolicitudCreate.as_view()), name= 'solicitud_crear' ),
    path('solicitud/editar/<pk>/', login_required(SolicitudUpdate.as_view()), name= 'solicitud_editar' ),
    path('solicitud/eliminar/<pk>/', login_required(SolicitudDelete.as_view()), name= 'solicitud_eliminar' ),
 	 
]
