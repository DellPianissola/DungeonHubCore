import pytest

from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories.core import *
from tests.factories.dharma import *


register(UserFactory)
register(NatureFactory)
register(WeaponFactory)


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
def weapon():
    return WeaponFactory()


@pytest.fixture
def user():
    return UserFactory()
