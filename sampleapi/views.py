from django.shortcuts import render

def usersApi(request):
    users = [
        {
            'name': 'Anurag'
            'role': 'backend'
        },
        {
            'name': 'Pranjal'
            'role': 'forntend'
        },
        {
            'name': 'Ayush'
            'role': 'flutter'
        }

    ]
