from django.conf.urls import patterns, include, url
from tasks.views import main_page, user_page
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', main_page),
    url(r'^user/(\w+)/$', user_page),
)
