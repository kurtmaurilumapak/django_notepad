from django.contrib import admin
from .models import Note
# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'note', 'created_at')  # Display fields in the admin list
    search_fields = ('title', 'note')  # Enable search by title or note content
    list_filter = ('user',)  # Add filter by user