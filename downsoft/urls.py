from django.conf.urls.defaults import *
from newsoft.resources import CATEGORY_DICT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

regex = '('+'|'.join(CATEGORY_DICT.keys()) + ')'
	

urlpatterns = patterns('',
    # Example:
    # (r'^downsoft/', include('downsoft.foo.urls')),
	(r'^softwares/(?P<os_type>[wlm])/$', 'newsoft.views.mainpage'), #check how to redirect default to w or record preference 
	(r'^softwares/(?P<category>'+regex+')/$', 'newsoft.views.mainpage'),
	(r'^softwares/(?P<os_type>[wlm])/(?P<soft_name>\w+)/$', 'newsoft.views.eachsoft'),
    (r'^softwares/upload/$', 'newsoft.views.uploadform'),
	(r'^softwares/search/$','newsoft.views.search'),
	(r'^comments/', include('django.contrib.comments.urls')),
	# (r'^softwares/browse/?q=(?P<q>)/$','softwares.views.search'),
    # (r'^softwares/success/$', 'softwares.views.upload'),
	# (r'^downsoft/upload/$','download.views.upload'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
	        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/gen/downloadSoft/downsoft/softwares/static_media/'}),
			    ) #use apache for static data remove after deployment    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

