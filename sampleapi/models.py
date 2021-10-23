from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=256)
# Create your models here.
class Article(models.Model):
    # def naming(self,title):
    #     self.title=title
    slug = models.SlugField(null= False, blank= False)
    title = models.CharField(max_length=256)
    description = models.TextField()
    body = models.TextField()
    tags = models.ManyToManyField('Tag')
    createdAt = models.DateTimeField(auto_now_add= True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    favourited = models.BooleanField()
    favouriteCount = models.IntegerField(default=0)
