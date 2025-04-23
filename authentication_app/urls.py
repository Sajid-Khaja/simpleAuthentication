from django.urls import path
from .views import register, user_login, user_logout, dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),  # Ensure this name matches
    path('logout/', user_logout, name='user_logout'),
    path('', dashboard, name='dashboard'),
]
