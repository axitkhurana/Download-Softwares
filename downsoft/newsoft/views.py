import os
import errno
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponse
from newsoft.models import Software, Version, Operatingsys
from newsoft.forms import AddSoftwareForm
from datetime import datetime
from resources import CATEGORY_DICT, CATEGORY_LIST, DEFAULT_OS
from settings import UPLOAD_DIR

def mainpage(request, os_type=DEFAULT_OS):
    """ returns a dictionary with key as category 
        & value as top 4 version entries accorrding to download
        count """
    top4={}
    for i in CATEGORY_LIST:
        top4[i[1]] = Version.objects.filter(operatingsys__software__category =
                i[0], operatingsys__os_type = os_type).order_by('-download_count')[:4]
    if request.method == 'POST':
        pass
        #form=SearchForm(request.POST) # delete this line Results here
    else:
        #show main page 'yo' here
        return render_to_response('index.html',{'category_dict':CATEGORY_DICT,'top4':top4}) #Iterate category in template , sort and slice(making a function for this) on basis of rating for top 4 and then pass as variables in template

def eachsoft(request, soft_name=None, os_type=DEFAULT_OS):
    """ view for software | particular name and os,all versions """
    try:
        onesoft = Version.objects.filter(operatingsys__software__soft_name__iexact = soft_name, operatingsys__os_type = os_type).order_by('-date_added')
        single_version = list(onesoft)[0]
        #render to response doesn't take care of csrf token
        #single_version = onesoft[:1].get() #.get() doesn't use cache , queries the database evertime
        related = Version.objects.filter(operatingsys__software__category = single_version.operatingsys.software.category, operatingsys__os_type = os_type).order_by('-download_count')[:12] #picks most downloaded same category software as related, add artificial intelligence based on user interaction
        tags = single_version.operatingsys.software.tags.split(',')
    except (Version.DoesNotExist, KeyError):
        raise Http404
    template_dict = {'onesoft': onesoft, 'tags':tags, 'single_version':single_version, 'related':related}
    return render_to_response('eachsoft.html', template_dict ,context_instance=RequestContext(request))

def search(request, os_type=DEFAULT_OS):
    "view for search"
    query = request.GET.get('q', '')
    results=[]
    #for sorting by most downloaded change -date_added to -download_count
    if query:
        #qset = (
        #   Q(soft_name__icontains=query) |
        #   Q(category__icontains=query) |
        #   Q(subcategory__icontains=query) |
        #   Q(tags__icontains=query) |
        #   Q(description__iconntains=query)
        #)
        r1 = Version.objects.filter(operatingsys__software__soft_name__icontains = query, operatingsys__os_type = os_type).order_by('-date_added')
        r2 = Version.objects.filter(operatingsys__software__category__icontains = query, operatingsys__os_type = os_type).order_by('-date_added')
        r3 = Version.objects.filter(operatingsys__software__subcategory__icontains = query, operatingsys__os_type = os_type).order_by('-date_added')
        r4 = Version.objects.filter(operatingsys__software__tags__icontains = query, operatingsys__os_type = os_type).order_by('-date_added')
        r5 = Version.objects.filter(operatingsys__software__description__icontains = query, operatingsys__os_type = os_type).order_by('-date_added')
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


#def group_soft(objects):
#    "groups software according to same name into classes"
#    group={}
#    for a in objects:
#        if a.soft_name not in  group:
#            group[a.soft_name]=[a,]
#        else:
#            group[a.soft_name].append(a)
#    return group
#
#
#def group_soft(objects):
#    "groups software according to same name"
#    group={}
#    for a in objects:
#        if a.soft_name not in  group:
#            group[a.soft_name]=[a,]
#        else:
#            group[a.soft_name].append(a)
#    return group
def categories(request):
    "view for main page"
    if request.method == 'POST':
        form=SearchForm(request.POST) # delete this line Results here
    else:
        #show main page 'yo' here
        return render_to_response('index.html',{'category_dict':CATEGORY_DICT,'top4':top4}) #Iterate category in template , sort and slice(making a function for this) on basis of rating for top 4 and then pass as variables in template


def mkdir_p(path):
    "mkdir -p functionality taking care of the race condition"
    try:
        os.makedirs(path)
    except OSError:
        if OSError.errno == errno.EEXIST: #directory already exists
            pass
        else:
            raise


def handle_uploaded_file(f, software):
    path = os.path.join(UPLOAD_DIR, software.category, software.subcategory,
            software.soft_name)
    if not os.path.exists(path):
        mkdir_p(path)
    destination = open(os.path.join(path,f.name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

class AlreadyExists(Exception):
    "Custom Exception for Already Existing Object"
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr('Object Already Exists of type: ' + self.value)

def uploadform(request):
    "view for upload form # check if parameters are required"
    if request.method == 'POST':
        form = AddSoftwareForm(request.POST, request.FILES)
        if form.is_valid():
            soft_name = form.cleaned_data['soft_name']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            subcategory = form.cleaned_data['subcategory']
            tags = form.cleaned_data['tags'] #parse these/use django taggify
            try:
                soft_object = Software.objects.get(soft_name__iexact=soft_name)
            except Software.DoesNotExist:
                soft_object = Software(soft_name=soft_name,
                        description=description,
                        category=category,
                        subcategory=subcategory, tags=tags)
                soft_object.save()
                os_type = form.cleaned_data['os_type']
                try:
                    os_object = Operatingsys.objects.get(os_type__iexact =
                            os_type, software = soft_object)
                except Operatingsys.DoesNotExist:
                    os_object = Operatingsys(os_type=os_type,
                            software=soft_object)
                    os_object.save()
                    version = form.cleaned_data['version']
                    link = form.cleaned_data['link']
                    # uploaded_by #integrate this with users
                    try:
                        version_object = Version.objects.get(version__iexact =
                                version, operatingsys = os_object)
                    except Version.DoesNotExist:
                        version_object = Version(version = version, operatingsys=os_object, link=link)
                        version_object.save()
                    else:
                        raise AlreadyExists('Version')
            handle_uploaded_file(request.FILES['file'], soft_object)
            return render_to_response('index.html')
        return render_to_response('index.html',{'form':form,},context_instance=RequestContext(request))
        form=AddSoftwareForm(request.POST)
    else:
        form=AddSoftwareForm()
    return render_to_response('uploadform.html',{'form':form,},context_instance=RequestContext(request))
