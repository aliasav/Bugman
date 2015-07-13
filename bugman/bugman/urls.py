from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings
from bugman import views
from bug import urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bugman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   #url(r'^$', landing_page),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bug/', include('bug.urls')),
    url(r'^$', views.landing_page),

) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	 # change static file serving technique during production
	 # use this only untill setup of nginx

if settings.DEBUG:
	urlpatterns = patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns