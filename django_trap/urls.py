# This file comes from admin_honeypot by Derek Payton (MIT license).
# See https://github.com/dmpayton/django-admin-honeypot
import django
from django_trap import views

try:
    from django.conf.urls import patterns, url
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import patterns, url

# Add /admin/login/ as a separate named view in Django 1.7+
if django.VERSION >= (1, 7):
    urlpatterns = [
        url(r'^login/$', views.AdminHoneypot.as_view(), name='login'),
        url(r'^.*$', views.AdminHoneypot.as_view(), name='index'),
    ]
else:
    urlpatterns = patterns('',
        url(r'^.*$', views.AdminHoneypot.as_view(), name='index'),
    )
