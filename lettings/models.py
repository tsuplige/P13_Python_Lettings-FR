from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Class Address, premet de créé de créé les objets address da la BDD

    Attrs:
        nummber (int):
            numéro de rue
        street (str):
            nom de la rue
        city (str):
            ville de l'adresse
        state (str)
            pays de l'adresse
        zip_code (int):
            code postal
        country_iso_code(str):
            Le code pays

    Methode:
        _str_: affiche la str réprésentant un objet address
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """Class Address, premet de créé de créé les objets address da la BDD

    Attrs:
        title (str):
            titre
        address (obj):
            objet addresse

    Methode:
        _str_: affiche la str réprésentant un objet letting
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Letting"
        verbose_name_plural = "Lettings"
