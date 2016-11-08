from django.contrib import admin
from .models import Navbar

# Register your models here.
class AdminNavbar(admin.ModelAdmin):
    list_display = [
        'uid', 'name','picture', 'link']
    ordering = ['uid']

admin.site.register(Navbar, AdminNavbar)