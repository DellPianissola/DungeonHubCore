import pytest

from django.urls import reverse


@pytest.mark.django_db
class TestAuthAPI:

    @pytest.fixture(autouse=True)
    def setup(self, api_client, user):
        self.api_client = api_client
        self.user_url = reverse("core:user-list")
        self.login_url = reverse("login")

        self.user_data= {
            "email": "test@test.com",
            "first_name": "Teste",
            "last_name": "Teste",
            "password": "Teste123"
        }

        self.login_data = {
            "email": "test@test.com",
            "password": "Teste123"
        }


    def test_login(self):
        self.api_client.post(self.user_url, self.user_data, format="json")
        response = self.api_client.post(self.login_url, self.login_data, format="json")

        assert response.status_code == 200
