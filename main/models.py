from django.db import models

#####################################################################
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

#####################################################################
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

#####################################################################
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
    more = models.CharField(
        max_length = 120, blank = True, default= '-')
    link = models.CharField(
        max_length = 120, blank = True, default= '-')

    # Méthods
    def __str__(self):
        return self.name


#####################################################################
class Projects(models.Model):
    """
        Stores content for my personal projects presentations
    """
    # Attributes
    uid = models.AutoField(db_index = True, primary_key = True)
    title = models.CharField(max_length = 200)
    corpus = models.TextField()
    posted_date = models.DateTimeField(db_index=True, auto_now_add=True)
    
    # Methods
    def __str__(self):
        return self.title

#####################################################################
class ProjectsDocs(models.Model):
    """
        Stores docs static links, doc file type etc for each 
        project document.
    """

    # Attributes
    uid = models.AutoField(db_index = True, primary_key= True)
    project_uid = models.ForeignKey(
        Projects , related_name='docs_set', blank=True, null=True)
    title = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    doc_icon = models.CharField(max_length = 200)

    # Methods
    def __str__(self):
        return self.title

#####################################################################
class FooterItems(models.Model):
    """
        Just a list of footer links and text for my webpages
    """
    uid = models.AutoField(db_index = True, primary_key= True)
    title = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    # Methods
    def __str__(self):
        return self.title
