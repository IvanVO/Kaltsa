from django.contrib import admin
from .models import Profile, MissingPerson, Clue


# Register your models here.
admin.site.register(Profile)
admin.site.register(MissingPerson)
admin.site.register(Clue)
