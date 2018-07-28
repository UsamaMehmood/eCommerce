from django.views.generic import FormView, TemplateView
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from store.forms import LoginForm, SignupForm
from store.models import Customer


@csrf_exempt
def authenticate_login(request):
    if request.method == 'GET':
        return render(request, 'basic.html', {'title': 'Invalid Request!',
                                              'text': 'You cannot access Login with this type of request'})

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request=request, username=username, password=password)
    if user:
        login(request=request, user=user)
        return HttpResponseRedirect(reverse('store:home'))
    return render(request, 'basic.html', {'title': 'Error', 'text': 'Username or password is incorrect'})

@csrf_exempt
def authenticate_logout(request):
    if request.method == 'GET':
        return render(request, 'basic.html', {'title': 'Invalid Request!',
                                              'text': 'You cannot access Login with this type of request'})

    logout(request)
    return HttpResponseRedirect(reverse('store:home'))


class Home(TemplateView):
    template_name = 'store/home.html'


class Signup(FormView):
    template_name = 'store/signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        customer = Customer(first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'],
                            username=form.cleaned_data['username'],
                            email=form.cleaned_data['email'],
                            password=form.cleaned_data['password'])
        customer.save()
        user = User.objects.get(email=customer.email, username=customer.username)
        login(request=self.request, user=user)
        return HttpResponseRedirect(reverse('store:home'))


class DummyApi(APIView):
    def get(self, request):
        name = request.GET.get('name', '')
        response = {
            'name': '{}'.format(name),
            'message': 'Hello there! How are you?'
        }
        return Response(response, status=status.HTTP_200_OK)
