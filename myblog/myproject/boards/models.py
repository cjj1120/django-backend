from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.
#Foreign key is to create relationship between the models and and create a proper relationship at the database level

#models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
class Post(models.Model):
    author = models.ForeignKey(setting.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) 
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    #when we call __str__() we will get a text (string) with a Post title.
    def __str__(self):
        return self.title
    
