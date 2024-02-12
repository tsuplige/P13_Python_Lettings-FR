import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Letting, Address
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
class TestLettingViews:
    """Classe de tests pour les vues associées aux lettings."""
    def setup_method(self):
        """Initialise les données nécessaires pour les tests."""

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

    def test_letting_index_page(self):
        """Teste l'affichage de la page d'index des lettings."""

        response = self.client.get(reverse('lettings_index'))

        assert response.status_code == 200
        assert b'<h1 class="page-header-ui-title'
        b' mb-3 display-6">Lettings</h1>' in response.content
        assertTemplateUsed(response, "lettings/index.html")

    def test_letting(self):
        """Teste l'affichage des détails d'un letting."""

        response = self.client.get(reverse('letting', kwargs={'letting_id': self.letting.id}))

        assert response.status_code == 200
        assert b'<h1 class="page-header-ui-title mb-3 '
        b'display-6">shrek&#x27;s house</h1>' in response.content
        assert b'<p>Example City, NY 12345</p>' in response.content
        assertTemplateUsed(response, "lettings/letting.html")

    def test_letting_with_wrong_id(self):
        """Teste le comportement lorsqu'un ID de letting incorrect est fourni."""

        response = self.client.get(reverse('letting', kwargs={'letting_id': 2}))

        assert response.status_code == 404
        print(response.content)
        assert b"<p><strong>Sorry, couldn\'t find the page</strong></p>" in response.content
        assertTemplateUsed(response, "404.html")
