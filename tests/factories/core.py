import factory

from core.user.models.user import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    first_name = factory.Faker("word")
    last_name = factory.Faker("word")
    password = factory.PostGenerationMethodCall("set_password", "senha123")
   