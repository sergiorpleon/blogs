from django.test import TestCase
from django.core.urlresolvers import reverse
# Create your tests here.

from models import *
from forms import *
from django.contrib.auth.models import User

class SimpleTest(TestCase):
	def test_views(self):
		newcat = Categoria.objects.create(titulo='Big1')
		newent = Entrada.objects.create(titulo='Big1', contenido='Bob1',categoria=newcat)
		
		
		res = self.client.get(reverse('listblog'))
		self.assertEqual(res.status_code, 200)

		res = self.client.get(reverse('detailblog', args=(1,)))
		self.assertEqual(res.status_code, 200)
	
		res = self.client.get(reverse('listblogcat', args=(1,)))
		self.assertEqual(res.status_code, 200)
		
		#self.assertTrue(self.client.login(username='lolo',password='lolo')
		#data={}
		#data['content']='comentario'
		#res = self.client.post(reverse('listblog',data))
		#self.assertEqual(res.status_code, 302)
		#self.assertEqual(Comentarios.object.count(), 1)
		
		#comentario = Comentarios.object.all()[0]