from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    people = [
        {'name':'jay','age':  19},
        {'name':'jay','age':  19}
    ]

    vegetables = ['Pumpkin','Tomato','Potatoe']

    return render(request,"index.html", context={'people':people,'vegetables':vegetables,'page':'home'})

def about(request):
    context = {'page':'about'}
    return render(request,"about.html",context)

def contact(request):
    context = {'page':'contact'}
    return render(request,"contact.html",context)

def success_page(rwquest):
    print("*"*10)
    return HttpResponse("<h1>Hey this is a success Page</h1>")