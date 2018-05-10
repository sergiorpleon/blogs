from django.contrib import admin
from models import *
# Register your models here.
from actions import export_as_csv

class EntradaAdmin(admin.ModelAdmin):
	list_display = ("titulo", "fecha","categoria", "comentarios", "blog_top")
	list_filter = ("categoria",)
	search_fields = ("categoria__titulo",)
	list_editable = ("titulo","categoria",)
	list_display_links = ("fecha",)
	actions = [export_as_csv]		#da error mimtyope css
	#raw_id_fields = ("categoria",)  #para cuenado se tenga muchas categorias
	#filter_horizontal = ('entity',)  #para many to many diplay super
	
	def comentarios(self, obj):
		total = obj.total_comentario()
		return total
	comentarios.allow_tags = True #permitir html
	#comentarios.admin_order_field = "titulo"
	
	
class EntradaInline(admin.StackedInline):
	model = Entrada
	extra = 1

class CategoriaAdmin(admin.ModelAdmin):
	search_fields = ("titulo",)
	inlines = [EntradaInline]
	
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Comentario)

