import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class test_oc_lettings_site:

    def setup_method(self):
        """
        Méthode de configuration pour initialiser les test.
        """

        self.client = Client()

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == 200
        assert b'Welcome to Holiday Homes' in response.content
