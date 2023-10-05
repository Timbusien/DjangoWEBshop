from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from items.models import ProductModel, CategoryModel
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
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title__icontains=q)

        return qs


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.all()

        return context


@login_required
def add_to_favorite(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)
    user = request.user

    if product in user.favorite_items.all():
        user.favorite_items.remove(product)
    else:
        user.favorite_items.add(product)

    return redirect('shop')


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


class ProfileView(TemplateView):
    template_name = 'profile.html'






