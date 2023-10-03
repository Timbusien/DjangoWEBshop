from django.shortcuts import render
from items.models import ProductModel
from django.views.generic import TemplateView, ListView, DetailView
# from django.http import HttpResponse
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


# def shop(request):
#     items = ProductModel.objects.all().order_by('-uploaded_at')
#     return render(request, 'shop.html', {'items': items})


# class Shopping_page(TemplateView):
#     template_name = 'shop.html'


class Shop_Page(ListView):
    template_name = 'shop.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'items'


    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title__icontains=q)

        return qs


class ShopDetail(DetailView):
    template_name = 'shop-details.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'items'

class RegisterView(TemplateView):
    template_name = 'signup.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class LogoutView(TemplateView):
    template_name = 'logout.html'




