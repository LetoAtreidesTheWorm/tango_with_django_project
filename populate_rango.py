import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                       'tango_with_django_project.settings')

import django

django.setup()

from rango.models import Category, Page

def populate():

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/', 'views':10},
        {'title': 'How to Think like a Computer Scientist',
          'url': 'http://www.greenteapress.com/thinkpython/', 'views':11},
        {'title':'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/turtorials/python/', 'views':12}
        ]

    django_pages = [

        {'title': 'Official Django Tutorial',
          'url': 'https://docs.djangoproject.com/en/2.1/intro/turtorial01/' , 'views':13},
        {'title':'Django Rocks',
          'url': 'http://www.djangorocks.com/' , 'views':14},
        {'title':'How to Tango with Django',
          'url': 'http://www.tangowithdjango.com/' , 'views':15,}

]

    other_pages = [
       {'title':'Bottle', 
          'url': 'https://bottlepy.org/docs/dev/' , 'views':16},
       {'title':'Flask',
          'url': 'http://flask.pocoo.org' , 'views':1}]

    cats = {'Python': {'pages': python_pages, 'views':17 },
        'Django': {'pages': django_pages, 'views':18},
        'Other Frameworks': {'pages': other_pages, 'views':19}}
    
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views = 0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, likes = 0, views = 0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c



if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

