from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'app.views.home', name='home'),
    
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/(\d+)', 'app.views.about', name='about'),

    
    url(r'^listblog/(\d+)', 'app.views.listblogcat', name='listblogcat'),
    url(r'^listblog/', 'app.views.listblog', name='listblog'),
    url(r'^detailblog/(\d+)', 'app.views.detailblog', name='detailblog'),

    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    #url('', RedirectView.as_view(url='/listblog/', permanent=True)),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
