from django.db import models
from django.contrib.auth.models import User

#from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Categoria(models.Model):
	titulo=models.CharField(max_length=140)
	
	def __str__(self):
		return self.titulo
		
class Entrada(models.Model):
	titulo=models.CharField(max_length=140)
	#contenido=models.TextField()
	contenido = RichTextUploadingField()
	imagen=models.ImageField(upload_to='photos/', null=True, blank=True, ) #requiere pillow
	fecha=models.DateTimeField(auto_now_add=True)
	categoria=models.ForeignKey(Categoria)
	#total_comentario=models.IntegerField(default=0)
	
	
	def __str__(self):
		return self.titulo
		
	def total_comentario(self):
		t = Comentario.objects.filter(entrada = self.pk).count()
		return t
	total_comentario.integer = True
		
	def blog_top(self):
		t = Comentario.objects.filter(entrada = self.pk).count()
		return t > 10
	blog_top.boolean = True
		
class Comentario(models.Model):
	contenido=models.TextField(max_length=300, verbose_name="Comentario")
	fecha=models.DateTimeField(auto_now_add=True)
	entrada=models.ForeignKey(Entrada)
	usuario=models.ForeignKey(User)
	
	def __str__(self):
		return self.contenido