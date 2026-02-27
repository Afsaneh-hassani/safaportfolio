from django.contrib import admin
from .models import Contact  # ← اینجا ContactMessage رو به Contact تغییر بده

@admin.register(Contact)  # ← اینجا هم
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'message', 'created_at']
    ordering = ['-created_at']