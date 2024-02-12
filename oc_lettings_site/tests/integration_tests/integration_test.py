import pytest
from django.test import Client
from lettings.models import Letting, Address
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
class IntegrationTest:

    def setup_method(self):
        """
        Méthode de configuration pour initialiser les objets Address, Letting,
        User et Profile avant le test.
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

    def integration_test(self):

        index_response = self.client.get('/')
        print("HIIIIIIIIIIIIIIIIIIIII")
        assert index_response.status_code == 200
        assert b'Welcome to Holiday Homes' in index_response.content
        assert b'Lettings' in index_response.content
        assert b'Profiles' in index_response.content

        profile_index_response = self.client.get('/profiles')

        assert index_response.status_code == 200
        assert b'Nobody' in profile_index_response.content
        assert b'Profiles' in profile_index_response.content
