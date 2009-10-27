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
	(r'^posts/(?P<story_id>\d+)/$', 'cs1120.stories.views.detail'),
	(r'^posts/(?P<story_id>\d+)/upvote/$', 'cs1120.stories.views.upvote'),
	(r'^posts/(?P<story_id>\d+)/downvote/$', 'cs1120.stories.views.downvote'),
	(r'^posts/newpost/$', 'cs1120.stories.views.newpost'),
	(r'^posts/addpost/$','cs1120.stories.views.addpost'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
