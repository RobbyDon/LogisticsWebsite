from django.contrib import admin
from .models import ContactMessage

admin.site.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')  # Adjust fields as needed
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
