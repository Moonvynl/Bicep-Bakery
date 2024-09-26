from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product

class GeneralView(TemplateView):
    template_name = 'shop/general.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})
