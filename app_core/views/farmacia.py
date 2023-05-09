from django.views import generic

from app_core.models import Farmacia, Producto


class IndexView(generic.TemplateView):
    template_name = 'pages/start_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['object_list'] = Producto.objects.all()[:5]
        context['text'] = 'Últimos productos'
        print(context['object_list'])
        return context
