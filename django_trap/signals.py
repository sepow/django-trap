# This file comes from admin_honeypot by Derek Payton (MIT license).
# See https://github.com/dmpayton/django-admin-honeypot
from django.dispatch import Signal

honeypot = Signal(providing_args=['instance', 'request'])
