from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Class Profile, premet de créé les objets profile da la BDD

    attrs:
        user (obj):
            objet correspondant a un utilisateur
        favorite_city (str):
            ville favorite

    Méthode:
        _str_: affiche la str réprésentant un objet Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
