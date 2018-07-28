from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('logout/', views.authenticate_logout, name='logout'),
    path('api/', views.DummyApi.as_view(), name='api'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.authenticate_login, name='login'),
]