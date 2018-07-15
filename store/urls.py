from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('api/', views.DummyApi.as_view(), name='api')
]