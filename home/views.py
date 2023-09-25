from django.shortcuts import render
from home.models import noticia

def home(request):

    noti = noticia.objects.order_by('-date')[:10]

    context = {
        'noticias': noti,
             
    }

    return render (request, 'home/home.html', context)

def noti_about (request, id):

    noti = noticia.objects.get(id=id)

    context = {
        'notic': noti,      
    }

    return render (request, 'home/noticia.html', context)
