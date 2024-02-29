from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.db.models import Count
from django.contrib.contenttypes.admin import GenericTabularInline
from . import models
# Register your models here.

@admin.register(models.Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price','trainee_count']
    list_editable = ['price']
    list_per_page = 10
    search_fields = ['name']

    @admin.display(ordering = 'trainee_count')
    def trainee_count(self, sport):
        return sport.trainee_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            trainee_count = Count('trainee')
        )

@admin.register(models.Trainee)
class TraineeAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','phone','ultimate_goal','suitable_period','sport_name']
    list_editable = ['suitable_period' , 'ultimate_goal']
    list_per_page = 10
    list_select_related = ['sport']
    ordering = ['first_name' , 'last_name']
    list_filter = ['sport','suitable_period']
    search_fields = ['first_name__istartswith']

    def sport_name(self, trainee):
        return trainee.sport.name
    
class ClassItemInline(admin.TabularInline):
    model = models.ClassItem

@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    autocomplete_fields = ['sport','coach']
    inlines = [ClassItemInline]
    list_display = ['id', 'class_name', 'capacity', 'level','sport','date','coach','start_time']
    list_editable = ['level','sport','start_time','coach']
    list_select_related = ['sport','coach']

@admin.register(models.Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name' , 'suitable_period']
    list_editable = ['suitable_period']
    search_fields = ['first_name__istartswith','first_name']


    

