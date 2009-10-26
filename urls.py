from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^cs1120/', include('cs1120.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	(r'^posts/$', 'cs1120.stories.views.index'),
	(r'^posts/(?P<story_id)\d+)/$', 'cs1120.stories.views.detail'),
	(r'^posts/(?P<story_id)\d+)/comments$', 'cs1120.stories.views.comments'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
