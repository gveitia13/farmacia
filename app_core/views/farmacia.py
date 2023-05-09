from django.views import generic

from app_core.models import Farmacia, Producto


class IndexView(generic.ListView):
    template_name = 'pages/start_page.html'
    queryset = Producto.objects.all().order_by('-pk')

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('search'):
            return qs.filter(nombre__icontains=self.request.GET.get('search'))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['farmacia'] = Farmacia.objects.first() if Farmacia.objects.exists() else None
        context['text'] = 'Últimos productos'
        print(context['object_list'])
        return context
