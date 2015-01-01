from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import ArchiveIndexView
from meublog.models import Artigo

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'meusite.views.home', name='home'),
    # url(r'^meusite/', include('meusite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ArchiveIndexView.as_view(model=Artigo, date_field='publicacao'))
)
