from django.contrib import admin

from .models import Club
from .models import Event
from .models import Announcment
from .models import ClubRepresentative
from .models import ClubMember
from .models import Reserves
from .models import Room
from .models import Student
from .models import University


admin.site.register(Club)
admin.site.register(Event)
admin.site.register(Announcment)
admin.site.register(ClubMember)
admin.site.register(ClubRepresentative)
admin.site.register(Room)
admin.site.register(Reserves)
admin.site.register(Student)
admin.site.register(University)


