from django.urls import path
from .views import custom_login, logout_view


urlpatterns = [
    path('', custom_login, name='login'),
    path('logout/', logout_view, name='logout'),
]