from django.contrib import admin
from .models import Target,Notices

# Register your models here.
class TargetDetails(admin.TabularInline):
	model=Target
class NoticeAdmin(admin.ModelAdmin):
	inlines = [TargetDetails]
admin.site.register(Notices,NoticeAdmin)