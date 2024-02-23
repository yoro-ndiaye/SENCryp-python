# Dans SENcrypt/models.py

from django.db import models
from django.contrib.auth.models import User

class EncryptedData(models.Model):
    algorithm_choices = [
        ('AES', 'AES'),
        ('DES', 'DES'),
        # Ajoutez d'autres algorithmes au besoin
    ]

    algorithm = models.CharField(max_length=50, choices=algorithm_choices, default='AES')
    input_data = models.TextField(default='')  # Spécification d'une valeur par défaut (dans cet exemple, une chaîne vide)
    secret_key = models.CharField(max_length=100)
    output_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Ajoutez d'autres champs utilisateur au besoin
