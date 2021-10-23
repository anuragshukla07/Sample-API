from django.contrib import admin
from sampleapi import models
# Register your models here.
admin.site.register([
    models.Article,
    models.Tag
])