from django.db import models
from django_extensions.db.fields import UUIDField
from django.contrib.auth.models import User
import datetime


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores bugs associated with a developer"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class Developer(models.Model):
	user = models.OneToOneField(User, related_name='developer', db_index=True)
	email = models.CharField(max_length=200, blank=False, null=True, db_index=True)
	guid = UUIDField(db_index=True)
	xp = models.CharField(max_length=20, null=True)
	badges = ListField(null=True)
	created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
	active_bugs = ListField(null=True)
	fixed_bugs = ListField(null=True)
	

