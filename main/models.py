from django.db import models

# Create your models here.

class Navbar(models.Model):
    """
        To facilitate devblog's navbar building and tidiness
        I build the navbar in a class and let the templates
        do the html for me.
    """

    # Variables

    # Attributes
    uid = models.AutoField(
        db_index = True, primary_key = True)
    name = models.CharField(max_length = 120)
    picture = models.CharField(max_length = 120)
    link = models.CharField(max_length = 120)

    # Méthods
    def __str__(self):
        return self.name
    
class ExpTable(models.Model):
    """
        Content and useful information for populating and
        formatting my experience field in my CV
    """

    # Attributes
    uid = models.AutoField(
        db_index = True, primary_key = True)
    name = models.CharField(max_length = 10)
    odd = models.CharField(max_length=20)
    date = models.CharField(max_length = 120)
    corpus = models.TextField()
    more = models.CharField(max_length = 120)

    # Méthods
    def __str__(self):
        return self.name

class FormationTable(models.Model):
    """
        Content and useful information for populating and
        formatting my formation field in my CV
    """

    # Attributes
    uid = models.AutoField(
        db_index = True, primary_key = True)
    name = models.CharField(max_length = 10)
    odd = models.CharField(max_length=20)
    date = models.CharField(max_length = 120)
    corpus = models.TextField()
    more = models.CharField(max_length = 120, null = True)

    # Méthods
    def __str__(self):
        return self.name