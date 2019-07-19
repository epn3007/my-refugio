from django.db import models

# Create your models here.

class Persona(models.Model):	
	nombre=models.CharField(max_length=50)
	apellidos=models.CharField(max_length=70)
	edad=models.IntegerField()
	telefono=models.CharField(max_length=12)
	email=models.EmailField()
	domicilio=models.TextField()

	class Meta:
		verbose_name='Persona'
		verbose_name_plural='Personas'
		ordering=['nombre']

	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos)		#cuando acceda al objeto devolvera este atributo

class Solicitud(models.Model):
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.DO_NOTHING)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()

	class Meta:
		verbose_name='Solicitud'
		verbose_name_plural='Solicitudes'
		
	def __str__(self):
		return self.persona	