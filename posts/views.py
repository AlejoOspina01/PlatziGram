""" Post views  """

#Django import
from django.shortcuts import render

#Utilites
from datetime import datetime

posts = [
    {
        'title':'Mont Blac',
        'user':{
            'name':'Juan Viro',
            'picture':'https://i.picsum.photos/id/490/60/60.jpg?grayscale&hmac=bRsTn-eEXK4Uo_EqO0FKHpua2_H_sEZHdVFdiccGWgM'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo':'https://i.picsum.photos/id/603/800/800.jpg?hmac=VANxlVkT7NcDHxNp7-oV75u5CXh50jJQ3nOO6FsfTNw'
    },
    {
        'title':'Jet',
        'user':{
            'name':'Katherine Sanchez',
            'picture':'https://i.picsum.photos/id/974/60/60.jpg?grayscale&hmac=OvVulJOwUv-dTMPgvNHrPoQ7WSX8pJzK0hkKxLwnY3Y'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo':'https://i.picsum.photos/id/1022/800/800.jpg?hmac=C_htzo7js3N5v19Y3ie4R9zuhsxLbXTu6VODE5CXXJE'
    },
    {
        'title':'Mont Blac',
        'user':{
            'name':'Alejandro Ospina',
            'picture':'https://i.picsum.photos/id/220/60/60.jpg?grayscale&hmac=zePoZddC0TDbLpXObeIT5WZSl44e4sSHIGU7AlwaipM'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs')  ,
        'photo': 'https://i.picsum.photos/id/821/800/800.jpg?hmac=dprIWVMGR_ZtJAoT9PdNXWxA0SepdlG5EwPw68OnVLc'      
    }        
]

def list_posts(request):
    return render(request,'feed.html',{'posts':posts})


