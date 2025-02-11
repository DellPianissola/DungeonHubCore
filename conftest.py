import pytest

from pytest_factoryboy import register

from rest_framework.test import APIClient

from tests.factories.core import UserFactory


register(UserFactory)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return UserFactory()
