
from django.contrib import admin

from making_queries.models import Blog, Author, Entry
from .models import Student, Teacher, School, Place, Restaurant, Champion


class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'champion_type', 'rank',)
    list_editable = ('rank',)
    ordering = ('rank',)


admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Champion, ChampionAdmin)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
