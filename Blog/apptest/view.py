from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'hello world!'
    return render(request, 'apptest/hello.html', context)