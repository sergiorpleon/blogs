from django import forms
from django.forms import ModelForm
from models import *

class ComentarioForm(ModelForm):
	class Meta:
		model = Comentario
		exclude = ("entrada","usuario",)
		
#from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget

#class PostForm(forms.ModelForm):
#    content = forms.CharField(widget=CKEditorUploadingWidget())