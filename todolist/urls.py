from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from tasks.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', main_page),

   # Session management
   url(r'^login/$', 'django.contrib.auth.views.login'),
   url(r'^logout/$', logout_page),
   url(r'^register/$', register_page),
   url(r'^register/success/$', TemplateView.as_view(template_name="registration/register_success.html")),

   # Account management
   (r'^save/$', todolist_save_page),
)
