from django.http import HttpResponse
import json

def usersApi(request):
    users = [
        {
            "name" : "Anurag",
            "role" : "backend"
        },
        {
            "name" : "Pranjal",
            "role" : "forntend"
        },
        {
            "name" : "Ayush",
            "role" : "flutter"
        }

    ]
    return HttpResponse(users)