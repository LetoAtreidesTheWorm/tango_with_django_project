from django.shortcuts import render

from django.shortcuts import HttpResponse

from rango.models import Category



def index(request):
    #return HttpResponse("<a href='/rango/about/'>About</a>")
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context= context_dict)

def about(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #return HttpResponse("BOMBOCLAAT <a href='/rango/home/'>Home</a>")
    return render(request, 'rango/about.html', context= context_dict)




