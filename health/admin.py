from django.contrib import admin
from .models import Bloodpressure, Glucoses

@admin.register(Bloodpressure)
class BloodpressureAdmin(admin.ModelAdmin):
    list_display = ["user","date","result1","result2","comment"]
    search_fields = ["user","date","result1","result2","comment"]
    list_filter = ["user","date","result1","result2","comment"]
    # autocomplete_fields = ['tags']
    # resource_class = BloodpressureResource


@admin.register(Glucoses)
class GlucosesAdmin(admin.ModelAdmin):
    list_display = ["user","date","result1","comment"]
    search_fields = ["user","date","result1","comment"]
    list_filter = ["user","date","result1","comment"]