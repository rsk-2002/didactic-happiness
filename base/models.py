from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="About me")
    job_title = models.CharField(verbose_name="Your service or job title", max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user

class SocialLink(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=400)
    social_links = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name



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