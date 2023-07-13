from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import django
settings.configure(DEBUG=True)

django.setup()
print(authenticate(username='admin', password='zh9468'))