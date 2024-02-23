from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import EncryptedData
from .models import UserProfile



# class EncryptionForm(forms.Form):
#     algorithm_choices = [
#         ('AES', 'AES'),
#         ('DES', 'DES'),
#         # Ajoutez d'autres algorithmes au besoin
#     ]

#     algorithm = forms.ChoiceField(
#         choices=algorithm_choices,
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
#     input_data = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control'}),
#         label='Enter Message'
#     )
#     secret_key = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         label='Enter Secret Key'
#     )

# class DecryptionForm(forms.Form):
#     algorithm_choices = [
#         ('AES', 'AES'),
#         ('DES', 'DES'),
#         # Ajoutez d'autres algorithmes au besoin
#     ]

#     algorithm = forms.ChoiceField(
#         choices=algorithm_choices,
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
#     input_data = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control'}),
#         label='Enter Message'
#     )
#     secret_key = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         label='Enter Secret Key'
#     )

# Dans SENcrypt/forms.py

from django import forms

class EncryptionForm(forms.Form):
    algorithm_choices = [
        ('AES', 'AES'),
        ('3DES', '3DES'),
        # Ajoutez d'autres algorithmes au besoin
    ]

    algorithm = forms.ChoiceField(choices=algorithm_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    input_data = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Entrer le texte à chiffrer')
    secret_key = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Entrer phrase de passe')

class DecryptionForm(forms.Form):
    algorithm_choices = [
        ('AES', 'AES'),
        ('3DES', '3DES'),
        # Ajoutez d'autres algorithmes au besoin
    ]

    algorithm = forms.ChoiceField(choices=algorithm_choices, widget=forms.Select(attrs={'class': 'form-control'}))
    encrypted_data = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Enter texte à déchiffrer')
    secret_key = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Entrer phrase de passe')



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    # Vous pouvez ajouter des champs supplémentaires ou des validations ici si nécessaire
    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user']
