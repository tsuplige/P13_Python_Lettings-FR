import pytest
from django.test import Client
from lettings.models import Letting, Address


@pytest.mark.django_db
class TestLettingModels:
    """Classe de test pour les modèles Letting et Address.

    Utilise pytest pour exécuter des tests de base de données Django.

    Attrs:
        client (Client): Client de test Django pour effectuer des requêtes HTTP.
        address (Address): Objet Address créé pour les tests.
        letting (Letting): Objet Letting créé pour les tests.
    """
    def setup_method(self):
        """
        Méthode de configuration pour initialiser les objets Address et Letting avant chaque test.
        """

        self.client = Client()

        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="Example City",
            state="NY",
            zip_code=12345,
            country_iso_code="USA")

        self.letting = Letting.objects.create(
                title="shrek's house",
                address=self.address,)

    def test_letting_model(self):
        """
        Teste la méthode __str__ de la classe Letting
        pour s'assurer qu'elle renvoie le titre correctement.
        """

        expected_value = "shrek's house"
        assert str(self.letting) == expected_value

    def test_address_model(self):
        """
        Teste la méthode __str__ de la classe Address
        pour s'assurer qu'elle renvoie l'adresse correctement.
        """
        expected_value = "123 Main St"
        assert str(self.address) == expected_value
