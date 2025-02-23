import os

import pytest

from django.urls import reverse

from tests.utils.get_test_image import get_test_image


@pytest.mark.django_db
class TestUserAPI:

    @pytest.fixture(autouse=True)
    def setup(self, api_client, nature):
        self.api_client = api_client
        self.api_client.force_authenticate(user=nature)
        self.list_url = reverse("dharma:nature-list")
        self.detail_url = reverse("dharma:nature-detail", args=[nature.id])

        self.data = {
            "name": "Teste",
            "points": "1",
            "description": "Teste",
            "image": get_test_image()
        }


    def test_create_nature(self):
        response = self.api_client.post(self.list_url, self.data, format="multipart")

        assert response.status_code == 201
        assert response.data["name"] == "Teste"

        os.remove('media/nature/test_image.png')


    def test_list_nature(self):
        response = self.api_client.get(self.list_url)

        assert response.status_code == 200
        assert isinstance(response.data, list)  # Retorna uma lista de usuários


    def test_retrieve_nature(self, nature):
        response = self.api_client.get(self.detail_url)

        assert response.status_code == 200
        assert response.data["name"] == nature.name


    def test_update_nature(self):
        data = {"name": "Updated"}

        response = self.api_client.patch(self.detail_url, data, format="json")

        assert response.status_code == 200
        assert response.data["name"] == "Updated"


    def test_delete_nature(self):
        response = self.api_client.delete(self.detail_url)

        assert response.status_code == 204