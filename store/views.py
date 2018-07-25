from django.views.generic import FormView, TemplateView
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from store.forms import LoginForm, SignupForm
from store.models import Customer


class Home(FormView):
    template_name = 'store/home.html'
    form_class = LoginForm

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return HttpResponse('Already Authenticated!')

        user = authenticate(request=self.request, username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request=self.request, user=user)
            return HttpResponse('You are logged in successfully!')
        else:
            form.add_error(None, error='Username or password is incorrect')
            context = self.get_context_data(**self.kwargs)
            context['form'] = form
            return render(self.request, 'store/home.html', context)


class Logout(LoginRequiredMixin, TemplateView):
    template_name = 'store/logout.html'
    login_url = reverse_lazy('store:home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('store:home'))

        return super(Logout, self).dispatch(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('store:home'))


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
