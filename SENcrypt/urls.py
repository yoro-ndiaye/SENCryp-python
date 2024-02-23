from django.urls import path
from .views import home, encrypt_view, decrypt_view, register_view, profile_view, login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('encrypt/', encrypt_view, name='encrypt'),
    path('decrypt/', decrypt_view, name='decrypt'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
