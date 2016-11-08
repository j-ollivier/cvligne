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

    # Méthodes
    def __str__(self):
        return self.name
    