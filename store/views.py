from django.views.generic import TemplateView
from django.shortcuts import render

class Home(TemplateView):
    template_name = 'store/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['page_title'] = 'Home'
        return context
