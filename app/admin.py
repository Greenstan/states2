from django.contrib import admin
from app.models import State, StateCapital, City

# Register your models here.

class StateCapAdmin(admin.StackedInline):
    model = StateCapital

class StateAdmin(admin.ModelAdmin):
    list_display=("name","abbreviation")
    inlines = (StateCapAdmin, )
    search_field = ['name']

admin.site.register(State, StateAdmin)
admin.site.register(StateCapital)
admin.site.register(City)
