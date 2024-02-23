from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import EncryptionForm, DecryptionForm, UserRegistrationForm, UserProfileForm
from .models import EncryptedData, UserProfile
from cryptography.fernet import Fernet
from django.urls import reverse_lazy

# Vue de connexion intégrée avec redirection vers la page d'accueil après la connexion réussie
login_view = LoginView.as_view(
    template_name='registration/login.html',
    authentication_form=AuthenticationForm,
    success_url=reverse_lazy('home') 
)

# Vue de déconnexion intégrée
logout_view = LogoutView.as_view()

def home(request):
    return render(request, 'home.html', {'form': EncryptionForm()})

@login_required
def encrypt_view(request):
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            algorithm = form.cleaned_data['algorithm']
            input_data = form.cleaned_data['input_data']
            secret_key = form.cleaned_data['secret_key']

            # Utilisation de la clé Fernet fixe
            fixed_key = b'k_zJ_4u8XShA1FIYQIpDXa9i5AZ6qvdYxYV4P0C5dGc='
            cipher_suite = Fernet(fixed_key)
            encrypted_data = cipher_suite.encrypt(input_data.encode())

            # Enregistrement des données chiffrées dans la base de données
            EncryptedData.objects.create(
                algorithm=algorithm,
                input_data=input_data,
                secret_key=secret_key,
                output_data=encrypted_data.decode()
            )

            return render(request, 'encrypt_result.html', {'result': encrypted_data.decode()})
    else:
        form = EncryptionForm()

    return render(request, 'encrypt.html', {'form': form})

@login_required
def decrypt_view(request):
    if request.method == 'POST':
        form = DecryptionForm(request.POST)
        if form.is_valid():
            algorithm = form.cleaned_data['algorithm']
            encrypted_data = form.cleaned_data['encrypted_data']

            # Utilisation de la clé Fernet fixe
            fixed_key = b'k_zJ_4u8XShA1FIYQIpDXa9i5AZ6qvdYxYV4P0C5dGc='

            # Déchiffrement avec Fernet
            cipher_suite = Fernet(fixed_key)
            decrypted_data = cipher_suite.decrypt(encrypted_data.encode())

            return render(request, 'decrypt_result.html', {'result': decrypted_data.decode()})
    else:
        form = DecryptionForm()

    return render(request, 'decrypt.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'registration/profile.html', {'user_profile': user_profile})
