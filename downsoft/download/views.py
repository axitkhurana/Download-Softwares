# Create your views here.
from django.template import Context,loader
from download.models import Category,Software
from django.http import HttpResponse

def index(request):
	categories=Category.objects.all()
	all_software=Software.objects.all().order_by('rating')
	t=loader.get_template('index.html')
	c=Context({'all_software':all_software},)
#	output=' '.join([p.soft_name for p in all_software])
	return HttpResponse(t.render(c))
