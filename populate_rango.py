import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')
import django
django.setup()

from rango.models import  Category, Page

def populate() :
    #First we will create lists of dictionaries containing the pages
    #we want to add into each category.
    #Then we will create a dictionary of dictionaries for our categories.
    #This might seem a little bit confusing, but it allows us to iterate
    #through each data structure, and add the data to our models.

    python_pages=[
        {'title':'Official Python Tutorial',
         'url':'http://docs.python.org/2/tutorial/' ,
         'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'title': 'Expert Python Programming, 2nd Edition',
         'url': 'https://github.com/PacktPublishing/Expert-Python-Programming_Second-Edition/'}]


    ]
