from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


class Home(TemplateView):
    template_name = 'store/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['page_title'] = 'Home'
        return context


class DummyApi(APIView):
    def get(self, request):
        name = request.GET.get('name', '')
        response = {
            'name': '{}'.format(name),
            'message': 'Hello there! How are you?'
        }
        return Response(response, status=status.HTTP_200_OK)
