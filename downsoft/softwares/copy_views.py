# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django import forms
from django.forms import ModelForm,Textarea
from softwares.models import Software
from softwares.forms import SoftwareForm
from datetime import datetime

def uploadform(request):
	if request.method == 'POST':
		form=SoftwareForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/softwares/success')
	else:
		form=SoftwareForm()
	return render_to_response('uploadform.html',{'form':form,},context_instance=RequestContext(request))

def upload(request):
	new_soft=Software(date_added=datetime.now(),download_count=0,show=False,link="default link",size=20,uploaded_by="backwas") #change default link
	form=SoftwareForm(request.POST,instance=new_soft)
	if form.is_valid():
		form.save()
		return render_to_response('index.html')
	return render_to_response('index.html',{'form':form,},context_instance=RequestContext(request))
