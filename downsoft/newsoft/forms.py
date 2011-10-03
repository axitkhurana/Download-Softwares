from newsoft.models import Software, Operatingsys, Version
from django import forms
from resources import CATEGORY_CHOICES,CATEGORY_TUPLE,OS_CHOICES



class AddSoftwareForm(forms.Form):
    soft_name = forms.CharField(max_length=30)
    description = forms.CharField(required=False,widget=forms.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_TUPLE)
    subcategory = forms.ChoiceField(choices=CATEGORY_CHOICES,required=False)
    forms.ChoiceField(choices=CATEGORY_CHOICES)#    server side check for sub cat & display only req sub cat using javascript
    tags = forms.CharField(required=False)#use django tags with suggestions
    version = forms.CharField(required=False) 
    os_type = forms.ChoiceField(choices=OS_CHOICES)
    link = forms.CharField(required=False) # link or file , atleast one
    filepath = forms.FileField()
