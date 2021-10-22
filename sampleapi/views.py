from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

class Student:
    name = "Anurag"
    roll_no = 20
    marks= 99

@api_view()
def usersApi(request):
   student=Student()
   return Response(student)