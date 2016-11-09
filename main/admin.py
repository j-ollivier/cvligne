from django.contrib import admin
from .models import Navbar , ExpTable, FormationTable

# Register your models here.
class AdminNavbar(admin.ModelAdmin):
    list_display = [
        'uid', 'name','picture', 'link']
    ordering = ['uid']

admin.site.register(Navbar, AdminNavbar)

class AdminExpTable(admin.ModelAdmin):
    list_display = [
        'uid', 'name','odd', 'corpus', 'more']
    ordering = ['uid']

admin.site.register(ExpTable, AdminExpTable)

class AdminFormationTable(admin.ModelAdmin):
    list_display = [
        'uid', 'name','odd', 'corpus', 'more']
    ordering = ['uid']

admin.site.register(FormationTable, AdminFormationTable)