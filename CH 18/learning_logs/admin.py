from django.contrib import admin

# Register your models here.

from .models import Topic, Entry

admin.site.register(Topic)  # Manage our model through the admin site

admin.site.register(Entry)
