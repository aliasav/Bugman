from django.contrib import admin
from bug.models import Bug

class BugAdmin(admin.ModelAdmin):
	list_display = ('guid', 'title', 'description', 'link', 'screenshot', 'guidelines', 'created_at', 'fixed_at', 'assigned_developer', 'reporter', 'category', 'status', 'priority')
	search_fields = ['guid', 'title', 'created_at', 'fixed_at', 'status', 'priority', 'reporter', 'category']

admin.site.register(Bug, BugAdmin)