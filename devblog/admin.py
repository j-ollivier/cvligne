from django.contrib import admin
from .models import Post
# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = [
        'uid', 'title','posted_date', 'category']
    ordering = ['posted_date']

admin.site.register(Post, AdminPost)
