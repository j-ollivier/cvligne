from django.db import models
from django.utils import timezone

#####################################################################
class Post(models.Model):
    """
        A simpe post model to populate the site's devblog.
    """

    # Variables pour les choix pré-remplis
    category_choices = (
        ('CV', 'CV'),
        ('Site', 'Site'),
        ('Serveur', 'Serveur'),
        ('Linux', 'Linux'),
        ('Divers', 'Divers'))

    # Attributes
    uid = models.AutoField(
        primary_key = True, db_index = True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_date = models.DateTimeField(
        db_index=True, auto_now_add=True)
    category = models.CharField(
        max_length = 100, choices = category_choices)

    # Méthodes
    def __str__(self):
        return self.title
