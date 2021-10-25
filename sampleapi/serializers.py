from rest_framework import serializers
from sampleapi import models

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many = True, read_only = True)
    class Meta:
        model = models.Article
        fields = '__all__'
