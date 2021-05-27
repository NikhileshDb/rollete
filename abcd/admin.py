from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(GameNumber)
class GameNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'id')

@admin.register(Sign)
class SignAdmin(admin.ModelAdmin):
    list_display = ('sign', 'id')

@admin.register(Dozen)
class DozenAdmin(admin.ModelAdmin):
    list_display = ('dozen', 'id')

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('column', 'id')