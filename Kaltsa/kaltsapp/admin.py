from django.contrib import admin
from .models import Municipio, State, Profile, MissingPerson, Clue


# Register your models here.
admin.site.register(Municipio)
admin.site.register(State)
admin.site.register(Profile)
admin.site.register(MissingPerson)
admin.site.register(Clue)
