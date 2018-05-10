from django.core.urlresolvers import reverse
from models import *

def menu(request):
	primera_cat = Categoria.objects.all()[0].pk
	primera_etrada = Entrada.objects.all()[0].pk
	menu = {'menu':[
		{'name': 'List-Blogs', 'url': reverse('listblog')},
		{'name': 'List-Blogs-Cat', 'url': reverse('listblogcat', args=(primera_cat,))},
		{'name': 'Detail-Blog', 'url': reverse('detailblog', args=(primera_etrada,))},
	]}
	
	for item in menu['menu']:
		if request.path == item['url']:
			item['active'] = True
	return menu