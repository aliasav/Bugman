from django.contrib import admin
from reporter.models import Reporter

class ReporterAdmin(admin.ModelAdmin):
	list_display = ('user', 'email', 'guid', 'xp', 'badges', 'created_at', 'bugs_reported', 'feedbacks')
	search_fields = ['email', 'xp', 'badges', 'bugs_reported']

admin.site.register(Reporter, ReporterAdmin)