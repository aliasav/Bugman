from django.contrib import admin
from developer.models import Developer

class DeveloperAdmin(admin.ModelAdmin):
	list_display = ('user', 'email', 'guid', 'xp', 'badges', 'created_at', 'active_bugs', 'fixed_bugs')
	search_fields = ['email', 'xp', 'badges', 'fixed_bugs']

admin.site.register(Developer, DeveloperAdmin)