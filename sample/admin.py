from django.contrib import admin
from . models import Movies_list, Movies_pics, Actors, Director
# Register your models here.

admin.site.register(Movies_list)
admin.site.register(Movies_pics)
admin.site.register(Actors)
admin.site.register(Director)