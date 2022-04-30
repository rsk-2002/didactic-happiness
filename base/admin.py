from django.contrib import admin
from .models import Project, Message, Skill
# Register your models here.

admin.site.register(Project)
admin.site.register(Message)
admin.site.register(Skill)