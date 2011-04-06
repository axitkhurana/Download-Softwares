from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^downsoft/', include('downsoft.foo.urls')),
	(r'^softwares/$', 'softwares.views.categories'),
    (r'^softwares/upload/$', 'softwares.views.uploadform'),
	(r'^softwares/browse/$','softwares.views.search'),
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
			    ) #use apache for static data remove after deployment
