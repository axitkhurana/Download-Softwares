#from django import forms
from softwares.models import Software
from django import forms
import re

class SoftwareForm(forms.ModelForm):
#	file=forms.FileField()
	class Meta:
		model=Software
		exclude=('link','date_added','size','download_count','show')#'uploaded_by',
	def clean_uploaded_by(self):
		data=self.cleaned_data['uploaded_by']
		user_pattern=re.compile(r'^([a-z0-9]{5})([dpuf])(ah|ap|bs|bt|cd|ce|ch|cn|cy|dm|dr|ec|ee|eq|es|hs|hy|ma|me|mt|nt|ph|pt|uc|wt)$')
		flag=user_pattern.match(data)
		if flag is None:
			raise forms.ValidationError("Username incorrect")
		return data

class SearchForm(forms.Form):
	search=forms.CharField(max_length=50)
