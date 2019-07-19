from django import forms
from apps.mascota.models import Mascota

#clase del formulario
class MascotaForm(forms.ModelForm):
	class Meta:
		model=Mascota

		#campos a utilizar
		fields=[
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',
		]

		#se escribe un diccionario
		labels={
			'nombre' : 'Nombre',
			'sexo' : 'Sexo',
			'edad_aproximada' : 'Edad aproximada',
			'fecha_rescate':'Fecha de rescate',
			'persona' : 'Adoptante',
			'vacuna' : 'Vacuna',
		}

		#widgets: Son los que se pintan en forma de etiquetas html
		widgets={
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
			'persona':forms.Select(attrs={'class':'form-control'}),		#este atributo es una llave foranea
			'vacuna':forms.CheckboxSelectMultiple(),	#este es un campo mucho a muchos	
		}