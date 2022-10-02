"""
WSGI config for django_cims project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_cims.settings')

# application = get_wsgi_application()

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_cims.settings')

# application = get_wsgi_application()

from whitenoise import WhiteNoise

from django_cims import MyWSGIApp()

application = MyWSGIApp()
application = WhiteNoise(application, root='cim_users/static/cim_users')
application.add_files('cim_users/static/cim_users', prefix='staticfiles')
