from django.views.generic import TemplateView
from .models import PropertyListing


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = PropertyListing.objects.all()
        return context