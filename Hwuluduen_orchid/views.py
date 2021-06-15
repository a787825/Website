from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class ProductView(TemplateView):
    template_name = 'product.html'

class InformationView(TemplateView):
    template_name = 'information.html'