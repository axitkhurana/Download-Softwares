from newsoft.models import Software,Operatingsys,Version#Comment
from django.contrib import admin

class SoftwareAdmin(admin.ModelAdmin):
    list_display=('soft_name','category','subcategory','tags')
    search_fields=('soft_name','tags')
    list_filter=('category',)
    #soft_name filter for different versions of same software
    #see ranges for download count and rating

admin.site.register(Software,SoftwareAdmin)
admin.site.register(Operatingsys)
admin.site.register(Version)
