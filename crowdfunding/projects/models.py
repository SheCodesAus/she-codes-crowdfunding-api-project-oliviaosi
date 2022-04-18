from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    # owner = models.CharField(max_length=200)
    owner= models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_prpjects'

    )
#relationship between category & project
    category= models.ForeignKey(
        'Category',
        null=True, 
        blank=True,
        on_delete=models.CASCADE,
        related_name='project_id'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous =models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete= models.CASCADE,
        related_name= 'pledges',
    ) 
    # supporter = models.CharField(max_length=200)
    support = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

