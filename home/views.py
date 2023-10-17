from django.shortcuts import render
from home.models import noticia
from django.core.paginator import Paginator

def home(request):

    noti = noticia.objects.order_by('-date')

    paginator = Paginator(noti, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'noticias': noti,
        "page_obj": page,
             
    }

    return render (request, 'home/home.html', context)

def noti_about (request, id):

    noti = noticia.objects.get(id=id)

    context = {
        'notic': noti,      
    }

    return render (request, 'home/noticia.html', context)
