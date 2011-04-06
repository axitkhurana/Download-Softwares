# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from newsoft.models import Software,Version,Os
from newsoft import resources
from newsoft.forms import SoftwareForm,SearchForm
from datetime import datetime
from resources import CATEGORY_DICT,CATEGORY_LIST
from django.db.models import Q
#import itertools
#from somewhere import handle_uploaded_file

#top 4 softwares for main page
top4={}
for i in CATEGORY_LIST:
	top4[i[1]]=Software.objects.filter(category=i[0]).order_by('-download_count')[:4]


def remove_duplicates(seq, idfun=None):  
	"removes duplicates from an iterable and returns a list w/o changing order"
	if idfun is None: 
		def idfun(x): return x 
	seen = {} 
	result = [] 
	for item in seq: 
		marker = idfun(item) 
		if marker in seen: continue 
		seen[marker] = 1 
		result.append(item) 
	return result

def group_soft(objects):
	"groups software according to same name into classes"
	group={}
	for a in objects:
		if a.soft_name not in  group:
			group[a.soft_name]=[a,]
		else:
			group[a.soft_name].append(a)
	return group

"""
def group_soft(objects):
	"groups software according to same name"
	group={}
	for a in objects:
		if a.soft_name not in  group:
			group[a.soft_name]=[a,]
		else:
			group[a.soft_name].append(a)
	return group
"""
def categories(request):
	"view for main page"
	if request.method == 'POST':
		form=SearchForm(request.POST) # delete this line Results here
	else:
		#show main page 'yo' here
		return render_to_response('index.html',{'category_dict':CATEGORY_DICT,'top4':top4}) #Iterate category in template , sort and slice(making a function for this) on basis of rating for top 4 and then pass as variables in template

def uploadform(request):
	"view for upload form"
	if request.method == 'POST':
		new_soft=Software(date_added=datetime.now(),download_count=0,show=False,link="default link",size=20,uploaded_by="backwas") #change default link
		form=SoftwareForm(request.POST, instance=new_soft)#request.FILES,
		if form.is_valid():
#			handle_uploaded_file(request.FILES['file'])
			form.save()
			return render_to_response('index.html')
		return render_to_response('index.html',{'form':form,},context_instance=RequestContext(request))
		form=SoftwareForm(request.POST)
	else:
		form=SoftwareForm()
	return render_to_response('uploadform.html',{'form':form,},context_instance=RequestContext(request))
"""
def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(soft_name__icontains=query) |
			Q(category__icontains=query) |
			Q(subcategory__icontains=query) |
			Q(tags__icontains=query) |
			Q(description__icontains=query)
		)
		results = Software.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("results.html", {"results":results,"query": query})

"""
def search(request):
	"view for search"
	query = request.GET.get('q', '')
	results=[]
	if query:
		#qset = (
		#	Q(soft_name__icontains=query) |
		#	Q(category__icontains=query) |
		#	Q(subcategory__icontains=query) |
		#	Q(tags__icontains=query) |
		#	Q(description__iconntains=query)
		#)
		r1 = Software.objects.filter(soft_name__icontains=query)
		r2 = Software.objects.filter(category__icontains=query)
		r3 = Software.objects.filter(subcategory__icontains=query)
		r4 = Software.objects.filter(tags__icontains=query)
		r5 = Software.objects.filter(description__icontains=query)
		#for a in itertools.chain(r1,r2,r3,r4,r5):
		#	results.append(a)
		results = list(r1)+list(r2)+list(r3)+list(r4)+list(r5)
		results=remove_duplicates(results) #pass os and filter os too!!


	#else:
	#	results = []
	return render_to_response("results.html", {"results":results,"query": query})
