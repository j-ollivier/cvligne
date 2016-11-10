from django.contrib import admin
from .models import Navbar , ExpTable, FormationTable, Projects, ProjectsDocs

#####################################################################
class AdminNavbar(admin.ModelAdmin):
    list_display = [
        'uid', 'name','picture', 'link']
    ordering = ['uid']

admin.site.register(Navbar, AdminNavbar)

#####################################################################
class AdminExpTable(admin.ModelAdmin):
    list_display = [
        'uid', 'name','odd', 'corpus', 'more']
    ordering = ['uid']

admin.site.register(ExpTable, AdminExpTable)

#####################################################################
class AdminFormationTable(admin.ModelAdmin):
    list_display = [
        'uid', 'name','odd', 'corpus', 'more']
    ordering = ['uid']

admin.site.register(FormationTable, AdminFormationTable)

#####################################################################
class AdminProjects(admin.ModelAdmin):
    list_display = [
        'uid', 'title', 'corpus']
    ordering = ['uid']

admin.site.register(Projects, AdminProjects)

#####################################################################
class AdminProjectsDocs(admin.ModelAdmin):
    list_display = [
        'uid', 'title', 'project_uid', 'doc_icon']
    ordering = ['uid']

admin.site.register(ProjectsDocs, AdminProjectsDocs)




