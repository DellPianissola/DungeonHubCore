import factory

from dharma.nature.models.nature import Nature
from dharma.technique.models.technique import Technique


class NatureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Nature

    name = factory.Faker("word")
    points = factory.Faker("random_int", min=0, max=100)
    description = factory.Faker("word")


class TechniqueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Technique

    name = factory.Faker("word")
    xp_cost = factory.Faker("random_int", min=0, max=100)
    type = factory.Faker("word")
    requirements = factory.Faker("word")
    effect = factory.Faker("word")
    description = factory.Faker("word")
