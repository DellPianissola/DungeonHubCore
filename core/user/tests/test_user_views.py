import pytest

from django.urls import reverse


@pytest.mark.django_db
class TestUserAPI:

    @pytest.fixture(autouse=True)
    def setup(self, api_client, user):
        self.api_client = api_client
        self.api_client.force_authenticate(user=user)
        self.list_url = reverse("core:user-list")
        self.detail_url = reverse("core:user-detail", args=[user.id])

        self.data = {
            "email": "test@test.com",
            "first_name": "Teste",
            "last_name": "Teste",
            "password": "Teste123"
        }


    def test_create_user(self):
        response = self.api_client.post(self.list_url, self.data, format="json")

        assert response.status_code == 201
        assert response.data["first_name"] == "Teste"


    def test_list_user(self):
        response = self.api_client.get(self.list_url)

        assert response.status_code == 200
        assert isinstance(response.data, list)  # Retorna uma lista de usuários


    def test_retrieve_user(self, user):
        response = self.api_client.get(self.detail_url)

        assert response.status_code == 200
        assert response.data["first_name"] == user.first_name


    def test_update_user(self):
        data = {"first_name": "Updated"}

        response = self.api_client.patch(self.detail_url, data, format="json")

        assert response.status_code == 200
        assert response.data["first_name"] == "Updated"


    def test_delete_user(self):
        response = self.api_client.delete(self.detail_url)

        assert response.status_code == 204