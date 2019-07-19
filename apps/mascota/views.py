from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota


# ESTA FUNCION ES PARA TRABAJAR UN JSON 
def listado(request):
	# lista = serializers.serialize('json', Mascota.objects.all() ) # MUestra todos los campos
	lista = serializers.serialize('json', Mascota.objects.all(), fields=['nombre', 'sexo'] )
	return HttpResponse(lista, content_type='application/json')


# Create your views here.
def index(request):
	#return HttpResponse("Index")
	return render(request, 'mascota/index.html')

#vista, recibe la peticion y se va a ejecutar (vista basada en funciones) se utilizaba antes y ya no se utilizan mucho
def mascota_view(request):
	if request.method=='POST':		#que es lo que va hacer nuestra vista
		form=MascotaForm(request.POST)	 #se reciben los datos que se estan mandando en el POST de nuestro formulario
		if form.is_valid():		#preguntams si los datos que se ingresaron son validos
			form.save()
		#return	redirect('mascota:mascota_listar')	#se redirecciona al index de mascota (urls.py)  tenia: return	redirect('mascota:index')
		return redirect('/mascota')
	else:
		form=MascotaForm()	#se ocupa cuando sea un GET
	return render(request, 'mascota/mascota_form.html', {'form':form})		#nombre del template (mascota/mascota_form.html)

def mascota_list(request):
	mascota=Mascota.objects.all().order_by('id')	#se crea el querySet
	contexto={'mascotas':mascota}		#se asigana el diccionario
	return render(request, 'mascota/mascota_list.html', contexto)		#se manda el nombre del template y se tambien tiene que manda el contexto

def mascota_edit(request, id_mascota):
	mascota=Mascota.objects.get(id=id_mascota)  #se genera el dataset 
	if request.method=='GET':
		form=MascotaForm(instance=mascota)   #instacia
	else:
		form=MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		#return redirect('mascota_listar')	#deberia de tener: return redirect('mascota:mascota_listar')
		return redirect('/mascota/listar')
	return render(request, 'mascota/mascota_form.html', {'form':form})		

def mascota_delete(request, id_mascota):
	mascota=Mascota.objects.get(id=id_mascota)
	if request.method=='POST':
		mascota.delete()
		return redirect('mascota_listar')
		#return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})


#VISTAS BASADAS EN CLASES a partir de la version 3.1

class MascotaList(ListView):
	model=Mascota
	template_name='mascota/mascota_list.html'
	paginate_by = 2

class MascotaCreate(CreateView):
	modelo =Mascota
	form_class=MascotaForm
	template_name='mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')

class MascotaUpdate(UpdateView):
	model=Mascota
	form_class=MascotaForm
	template_name='mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')


class MascotaDelete(DeleteView):
	model=Mascota
	template_name='mascota/mascota_delete.html'
	success_url = reverse_lazy('mascota:mascota_listar')

