from softwares.models import Software,Comment
from django.contrib import admin

class SoftwareAdmin(admin.ModelAdmin):
	list_display=('soft_name','os','version','category','show','subcategory','tags')
	search_fields=('soft_name','description','uploaded_by','tags')
	list_filter=('os','date_added','category','rating','download_count','show')#soft_name filter for different versions of same software, see ranges for download count and rating

admin.site.register(Software,SoftwareAdmin)
admin.site.register(Comment)
