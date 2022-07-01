from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'done')# fields of models that we will see in the list
    list_display_links = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description') # defines which fields we can search by
    list_editable = ('done',)
    list_filter = ('id', 'done')


admin.site.register(Todo, TodoAdmin)