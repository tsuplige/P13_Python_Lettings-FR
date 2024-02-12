import pytest
from django.urls import reverse
from django.test import Client
from profiles.models import Profile
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
class TestProfilesViews:
    """Classe de tests pour les vues associées aux profiles."""

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

    def test_profiles_index_page(self):
        """Teste l'affichage de la page d'index des profiles."""

        response = self.client.get(reverse('profiles_index'))

        assert response.status_code == 200
        assert b'<h1 class="page-header-ui-title'
        b' mb-3 display-6">Profiles</h1>' in response.content
        assertTemplateUsed(response, "profiles/index.html")

    def test_profile(self):
        """Teste l'affichage des détails d'un profile."""

        response = self.client.get(reverse('profile', kwargs={'username': self.profile.user}))

        assert response.status_code == 200
        assert b'<h1 class="page-header-ui-title'
        b' mb-3 display-6">Nobody</h1>' in response.content
        assert b'<p><strong>First name :</strong> Cloud</p>' in response.content
        assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_with_wrong_id(self):
        """Teste le comportement lorsqu'un ID de profile incorrect est fourni."""

        response = self.client.get(reverse('profile', kwargs={'username': 'heartless'}))

        assert response.status_code == 404
        print(response.content)
        assert b"<p><strong>Sorry, couldn\'t find the page</strong></p>" in response.content
        assertTemplateUsed(response, "404.html")
