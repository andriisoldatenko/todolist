from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import os.path
from django.conf import settings
from tasks.views import *

site_media = os.path.join(
    os.path.dirname(__file__), 'static'
)

urlpatterns = patterns('',
   url(r'^$', main_page),
   url(r'^tasks/', include('tasks.urls')),
   # Session management
   url(r'^login/$', 'django.contrib.auth.views.login'),
   url(r'^logout/$', logout_page),
   url(r'^register/$', register_page),
   url(r'^register/success/$', TemplateView.as_view(template_name="registration/register_success.html")),

   # Account management
   # (r'^create/$', task_save_page),
   url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.STATICFILES_DIRS} ),
)
