from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext

from models import *
from forms import *

from django.core.paginator import Paginator, InvalidPage, EmptyPage


from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return HttpResponse('Hola')
	
def about(request, num):
	return render(request,'about.html', dict(id = num))
	
def listblog(request):
	entradas = Entrada.objects.all().order_by('-fecha')
	categorias = Categoria.objects.all()
	
	
	
	paginator=Paginator(entradas, 10)
	
	try: pagina = int(request.GET.get("page",'1'))
	except ValueError : pagina = 1
	
	try:
		entradas = paginator.page(pagina)
	except (InvalidPage, EmptyPage):
		entradas = paginator.pagina(paginator.num_pages)
	
	return render(request,'listblogs.html', 
	                       dict(entradas = entradas, 
						        categorias = categorias))
								
def listblogcat(request, id):
	categorias = Categoria.objects.all()
	cat = Categoria.objects.get(pk = id)
	entradas = Entrada.objects.filter(categoria = cat).order_by('-fecha')
	
	

	totales=[]
	for ent in entradas:
		t = Comentario.objects.filter(entrada = ent).count()
		totales.append(t)
		
		
		
	paginator=Paginator(entradas, 10)
	
	try: pagina = int(request.GET.get("page",'1'))
	except ValueError : pagina = 1
	
	try:
		entradas = paginator.page(pagina)
	except (InvalidPage, EmptyPage):
		entradas = paginator.pagina(paginator.num_pages)
	
	return render(request,'listblogs.html', 
	                       dict(entradas = entradas,
						   		totales = totales,
						        categorias = categorias))
								
def detailblog(request, id):
	entrada = Entrada.objects.get(pk = id)
	total = Comentario.objects.filter(entrada = entrada).count()
	if request.method == "POST":
		form = ComentarioForm(request.POST)
		if form.is_valid():
			comentario = form.save(commit=False)
			comentario.entrada = entrada;
			comentario.usuario = request.user;
			comentario.save()
			
			#entrada.total_comentario = total+1;
			#entrada.save()
			 
	form = ComentarioForm()
	categorias = Categoria.objects.all()
	
	comentarios = Comentario.objects.filter(entrada = entrada)
	#return  render_to_response('detailblog.html', context_instance = RequestContext(request, locals()))
	return render(request,'detailblog.html', 
	                       dict(entrada = entrada, 
						        categorias = categorias,
								comentarios = comentarios,
								form = form))