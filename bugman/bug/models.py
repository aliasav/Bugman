from django.db import models
from django_extensions.db.fields import UUIDField
from developer.models import Developer
from reporter.models import Reporter
from multiselectfield import MultiSelectField
import datetime


# Create your models here.
class Bug(models.Model):
	guid = UUIDField(db_index=True)
	title = models.CharField(max_length=100, null=False, blank=False, db_index=True)
	description = models.TextField(max_length=600, blank=True, null=True)
	link = models.URLField(max_length=300, blank=True, null=True)
	screenshot = models.ImageField(upload_to='bugs_screenshots', null=True, blank=True)
	guidelines = models.TextField(blank=True, null=True)

	# datetime fields
	created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
	fixed_at = models.DateTimeField(null=True)
	
	# foreign keys
	assigned_developer = models.ForeignKey(Developer, related_name='assigned_developer', db_index=True)  
	reporter = models.ForeignKey(Reporter, related_name='reporter', db_index=True)

	# Bugs categories
	type1 = 'functional'
	type2 = 'logical'
	type3 = 'UI'
	type4 = 'design'
	type5 = 'typographical'
	type6 = 'system'
	type7 = 'standards'
	type8 = 'requirements'
	CATEGORY_LIST = (
		(type1, 'Functional'),
		(type2, 'Logical'),
		(type3, 'UI'),
		(type4, 'Design'),
		(type5, 'Typographical'),
		(type6, 'System'),
		(type7, 'Standards'),
		(type8, 'Requirements'),
		)

	# Bug Statuses : (Open -> Assigned -> Closed) or (Open -> Assigned -> Cancelled or Deferred) or (Open -> Cancelled or Deferred)
	status1 = 'open'
	status2 = 'closed'
	status3 = 'cancelled'
	status4 = 'deferred'
	status5 = 'assigned'
	STATUS_LIST = (
		(status1, 'Open'),
		(status2, 'Closed'),
		(status3, 'Cancelled'),
		(status4, 'Deferred'),
		(status5, 'Assigned')
		)

	# Priority
	p1 = '1'
	p2 = '2'
	p3 = '3'
	p4 = '4'
	p5 = '5'
	PRIORITY_LIST = (
		(p1, '1'),
		(p2, '2'),
		(p3, '3'),
		(p4, '4'),
		(p5, '5')
		)

	# choice fields
	category = MultiSelectField(choices=CATEGORY_LIST, null=False, blank=False, db_index=True)
	status = models.CharField(max_length=30, choices=STATUS_LIST, null=False, db_index=True)
	priority = models.CharField(max_length=2, choices=PRIORITY_LIST, null=False, db_index=True)

	def __unicode__(self):
		return '%s <--> %s : %s, %s, %s ' % (self.title, self.guid, self.reporter, self.status, self.category,)

