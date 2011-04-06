# Create your views here.
from django.http import HttpResponse
"""
def display1(request):
	try:
		ua=request.META['HTTP_USER_AGENT']
	except KeyError:
		ua='unknown'
	return HttpResponse("Your Browser is %s" % ua)
"""
def display(request):
	values=request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))
"""
def displayi(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))
	"""
