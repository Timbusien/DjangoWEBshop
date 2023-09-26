from django.shortcuts import render
from django.http import HttpResponse
# from items.forms import NewForm

# Create your views here
# def start(requests):
#     return HttpResponse('Hi!\n\n\n'
#                         'lorem ipsum dspgihfd;ohdg dkfhldfjn lkdshld sdlkfh ldkg')
#
#
# def about(requests):
#     return HttpResponse("i don't who we are")
#
#
# def contact(requests):
#     return HttpResponse('+99894')
#
#
# def simple(request):
#     return render(request, "index.html",)
#
#
# def form(request):
#     context = {}
#
#     form = NewForm(request.POST)
#     context['form'] = form
#
#     return render(request, 'index.html', context)


def home(request):
    return render(request, 'index.html', {})



