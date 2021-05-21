""" Post views  """

#Django import
from django.http import HttpResponse, JsonResponse

#Utilites
from datetime import datetime

posts = [
    {
        'name':'Mont Blac',
        'user':'Juan Viro',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://i.picsum.photos/id/503/200/300.jpg?hmac=NvjgwV94HmYqnTok1qtlPsDxdf197x8fsWy5yheKlGg'
    },
    {
        'name':'Jet',
        'user':'Katherine SAnchez',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://i.picsum.photos/id/830/200/300.jpg?hmac=YHS3854_x-GHeQToxsiUmEvBJpDbZOAyixX9nxz61Sg'
    },
    {
        'name':'Mont Blac',
        'user':'Juan Viro',
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://i.picsum.photos/id/825/200/300.jpg?hmac=02AaqBOvx8gwrGt7a3HWzJHnZXrMzYoXbAYwjJWH40E'
    }        
]

def list_posts(request):
    content = []
    for post in posts:
        content.append(""" 
            <p> <strong> {name} </strong></p>
            <p> <small> {user} - <i>{timestamp}</i> </small></p>
            <figure> <img src="{picture}"/> </figure>
         """.format(**post))
    return HttpResponse('<br>'.join(content))


