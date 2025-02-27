import pytest

from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories.core import UserFactory
from tests.factories.dharma import NatureFactory, TechniqueFactory


register(UserFactory)
register(NatureFactory)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def nature():
    return NatureFactory()


@pytest.fixture
def technique():
    return TechniqueFactory()


@pytest.fixture
def user():
    return UserFactory()
