from django.contrib import admin

from .models import Club
from .models import Event
from .models import Announcment

admin.site.register(Club)
admin.site.register(Event)
admin.site.register(Announcment)

