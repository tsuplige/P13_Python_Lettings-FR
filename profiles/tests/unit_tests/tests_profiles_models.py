import pytest
from django.test import Client
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestProfilesModels:

    def setup_method(self):
        """
        Méthode de configuration pour initialiser les objets Profile
        et User avant chaque test.
        """

        self.client = Client()

        self.user = User.objects.create(
            username="Nobody",
            password="genesis",
            first_name="Cloud",
            last_name="Strif",
            email="soldat@contact.mi",
        )

        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="the world that never was")

    def test_profile_model(self):
        """
        Teste la méthode __str__ de la classe profile
        pour s'assurer qu'elle renvoie le username correctement.
        """

        expected_value = "Nobody"
        assert str(self.profile) == expected_value
        assert str(self.profile.favorite_city) == "the world that never was"
        assert str(self.profile.user.first_name) == "Cloud"
