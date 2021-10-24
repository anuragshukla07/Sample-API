from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from sampleapi import serializers,models
from rest_framework.generics import (
  ListAPIView,
  RetrieveAPIView,
  UpdateAPIView,
  ListCreateAPIView,
  RetrieveUpdateAPIView
)
class ArticlesListView(ListCreateAPIView):
  queryset = models.Article.objects.all()
  serializer_class=serializers.ArticleSerializer

class ArticlesDetailView(RetrieveUpdateAPIView):
  queryset = models.Article.objects.all()
  serializer_class=serializers.ArticleSerializer