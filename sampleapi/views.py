from rest_framework.decorators import api_view
from rest_framework.response import Response
from sampleapi import serializers,models


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks



@api_view()
def articleApi(request):
  articles = models.Article.objects.all()
  response = serializers.ArticleSerializer(articles, many = True)
  return Response(response.data)

@api_view()
def usersApi(request):
    student1 = Student("anurag", 20, 99)
    student2 = Student("pranjal", 30, 95)
    student3 = Student("sameer", 40, 97)
    response = serializers.StudentSerializer([
      student1,
      student2,
      student3
    ], many=True)
    return Response(response.data)
