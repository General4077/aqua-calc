from django.contrib import admin

from .models import Crop, Media, Filter, SystemType, System

admin.site.register(Media)
admin.site.register(Crop)
admin.site.register(Filter)
admin.site.register(SystemType)
admin.site.register(System)
