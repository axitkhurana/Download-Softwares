from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,Http404,HttpResponse
from newsoft.models import Software,Version,Operatingsys
#from newsoft.forms import SoftwareForm,SearchForm
from datetime import datetime
from resources import CATEGORY_DICT,CATEGORY_LIST,DEFAULT_OS
#from django.db.models import Q
#import itertools
#from somewhere import handle_uploaded_file

def mainpage(request, os_type=DEFAULT_OS):
    """ returns a dictionary with key as category 
        & value as top 4 version entries accorrding to download
        count """
    top4={}
    for i in CATEGORY_LIST:
        top4[i[1]] = Version.objects.filter(os_type__software__category = i[0], os_type__os_type = os_type).order_by('-download_count')[:4]
    if request.method == 'POST':
        pass
        #form=SearchForm(request.POST) # delete this line Results here
    else:
        #show main page 'yo' here
        return render_to_response('index.html',{'category_dict':CATEGORY_DICT,'top4':top4}) #Iterate category in template , sort and slice(making a function for this) on basis of rating for top 4 and then pass as variables in template

def eachsoft(request, soft_name=None, os_type=DEFAULT_OS):
    """ view for software | particular name and os,all versions """
    try:
        onesoft = Version.objects.filter(os_type__software__soft_name__iexact = soft_name, os_type__os_type = os_type).order_by('-date_added')
        single_version = list(onesoft)[0]
        #render to response doesn't take care of csrf token
        #single_version = onesoft[:1].get() #.get() doesn't use cache , queries the database evertime
        related = Version.objects.filter(os_type__software__category = single_version.os_type.software.category, os_type__os_type = os_type).order_by('-download_count')[:12] #picks most downloaded same category software as related, add artificial intelligence based on user interaction
        tags = single_version.os_type.software.tags.split(',')
    except (Version.DoesNotExist, KeyError):
        raise Http404
    template_dict = {'onesoft': onesoft, 'tags':tags, 'single_version':single_version, 'related':related}
    return render_to_response('eachsoft.html', template_dict ,context_instance=RequestContext(request))

def search(request, os_type=DEFAULT_OS):
    "view for search"
    query = request.GET.get('q', '')
    results=[]
    if query:
        #qset = (
        #   Q(soft_name__icontains=query) |
        #   Q(category__icontains=query) |
        #   Q(subcategory__icontains=query) |
        #   Q(tags__icontains=query) |
        #   Q(description__iconntains=query)
        #)
        r1 = Version.objects.filter(os_type__software__soft_name__icontains = query, os_type__os_type = os_type).order_by('-download_count')
        r2 = Version.objects.filter(os_type__software__category__icontains = query, os_type__os_type = os_type).order_by('-download_count')
        r3 = Version.objects.filter(os_type__software__subcategory__icontains = query, os_type__os_type = os_type).order_by('-download_count')
        r4 = Version.objects.filter(os_type__software__tags__icontains = query, os_type__os_type = os_type).order_by('-download_count')
        r5 = Version.objects.filter(os_type__software__description__icontains = query, os_type__os_type = os_type).order_by('-download_count')
        #for a in itertools.chain(r1,r2,r3,r4,r5):
        #   results.append(a)
        results = list(r1)+list(r2)+list(r3)+list(r4)+list(r5)
        results=remove_duplicates(results)

    #else:
    #   results = []
    return render_to_response("results.html", {"results":results,"query": query})

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

"""
def group_soft(objects):
    "groups software according to same name into classes"
    group={}
    for a in objects:
        if a.soft_name not in  group:
            group[a.soft_name]=[a,]
        else:
            group[a.soft_name].append(a)
    return group


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
#           handle_uploaded_file(request.FILES['file'])
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

