import os
import pytest
import tempfile

from django.conf import settings
from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories.core import UserFactory
from tests.factories.dharma import NatureFactory


register(UserFactory)
register(NatureFactory)


@pytest.fixture(scope='function')
def media_root():
    # Cria um diretório temporário para testes
    temp_dir = tempfile.mkdtemp()
    settings.MEDIA_ROOT = temp_dir
    yield temp_dir
    # Limpa o diretório temporário após o teste
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def nature():
    return NatureFactory()


@pytest.fixture
def user():
    return UserFactory()
