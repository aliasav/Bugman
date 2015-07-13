from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings
from bug import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'report$', views.report_bug ),
) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	 # change static file serving technique during production
	 # use this only untill setup of nginx