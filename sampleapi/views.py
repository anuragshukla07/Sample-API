from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

@api_view()
def usersApi(request):
    users = [
        {
            "name" : "Anurag",
            "role" : "backend"
        },
        {
            "name" : "Pranjal",
            "role" : "frontend"
        },
        {
            "name" : "Ayush",
            "role" : "flutter"
        }

    ]
    return Response(users)