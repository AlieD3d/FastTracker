from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


data_db = [
    {'id': 1, 'title': 'Сделать капчу', 'content': 'Реализовать капчу dfgdfgdf gfhfghfghfghfgh', 'is_published': True},
    {'id': 2, 'title': 'Сделать sdfsdf', 'content': 'Реализовать sdfsdf 12312fdgdfg', 'is_published': True},
    {'id': 3, 'title': 'Сделать sdfsdf', 'content': 'Реализовать hgfjghj fvbnhjlkq4234', 'is_published': True},
    {'id': 4, 'title': 'Сделать sdfsdfgdfgdf', 'content': 'Реалиdfgdfgзовать 345gfhfdgfgh', 'is_published': True},
    {'id': 5, 'title': 'Сделать sdfdfgdfgsdf', 'content': 'Реализdfgdfgовать wdsffdgh345', 'is_published': True},
    {'id': 6, 'title': 'Сделатьdfgdfg sdfdfgdfgsdf', 'content': 'Реализdfgdfgовать q12e4dfgghfgh', 'is_published': True},

]


def index(request):
    data = {
        'posts': data_db,
    }
    return render(request, 'tracker/index.html', context=data)


def show_post(request, post_id):
    return HttpResponse(f"Отображение статтю {post_id}")


def about(request):
    return render(request, 'tracker/about.html')


def addtask(request):
    return render(request, 'tracker/addtask.html')


def login(request):
    return render(request, 'tracker/login.html')


def registration(request):
    return render(request, 'tracker/registration.html')

def contact(request):
    return render(request, 'tracker/contact.html')


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1> Страница не найдена :( </h1>")


