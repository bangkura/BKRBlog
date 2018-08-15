from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def hello(request):
    context = {}
    context['hello'] = 'hello world!'
    return render(request, 'appTest/hello.html', context)

def mouth(request):
    return render(request, 'appTest/mouth.html', {});

@csrf_exempt
def save(request):
    if request.GET:
        return HttpResponse('yep')
    if not 'blog' in request.POST:
        return HttpResponse('yep')
    return request.POST['blog'];