from pyexpat import model
from django.db import models

# Create your models here.

# this is to check the status of a post
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

ARTICAL_TYPE = (
    (0, "Travel Dev"),
    (1, "Game Dev"),
    (2, "Web Dev")
)

# this is for making tables in the database
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # put an opton for a profile picuture here
    status = models.IntegerField(choices=STATUS, default=0)
    artical_type = models.IntegerField(choices=ARTICAL_TYPE, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title