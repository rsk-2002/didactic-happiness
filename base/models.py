from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200) 
    thumbnail = models.ImageField(null=True)
    source_code = models.URLField(max_length=255)
    live_link = models.URLField(max_length=255)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    level = models.IntegerField()

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name