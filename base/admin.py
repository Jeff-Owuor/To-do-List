from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','created','complete')
    search_fields = ('title',)
    admin.site.site_header = 'To-do List'
    
    

# Register your models here.
admin.site.register(Task,TaskAdmin)