from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import exproj.index
print 'indexfile:', exproj.index.__file__
import exproj.index.views
print exproj.index.views

urlpatterns = patterns('',
    url(r'^$', 'exproj.index.views.index'),
    url(r'^spotnet/', include('spotnet.urls', namespace='spotnet')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)