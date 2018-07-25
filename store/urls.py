from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('api/', views.DummyApi.as_view(), name='api'),
    path('signup/', views.Signup.as_view(), name='signup'),
]