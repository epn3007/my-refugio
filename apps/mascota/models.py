from django.db import models

from apps.adopcion.models import Persona

class Vacuna(models.Model):
	nombre=models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)    #devuelve el nombre de los adoptantes

class Mascota(models.Model):
	nombre=models.CharField(max_length=50)
	sexo=models.CharField(max_length=10)
	edad_aproximada=models.IntegerField()
	fecha_rescate=models.DateField()
	persona=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	vacuna=models.ManyToManyField(Vacuna, blank=True)

	class Meta:
		verbose_name='Mascota'
		verbose_name_plural='Mascotas'
		ordering=['nombre']

	def __str__(self):
		return self.nombre	