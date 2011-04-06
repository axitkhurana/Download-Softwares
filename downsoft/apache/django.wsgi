import os
import sys

path = '/home/gen/downloadSoft'
if path not in sys.path:
	sys.path.append(path)
sys.path.append('/home/gen/downloadSoft/downsoft')


os.environ['DJANGO_SETTINGS_MODULE'] = 'downsoft.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
