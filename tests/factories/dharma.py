import factory

from dharma.nature.models.nature import Nature


class NatureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Nature

    name = factory.Faker("word")
    points = factory.Faker("random_int", min=0, max=100)
    description = factory.Faker("word")
    # image = factory.django.ImageField()
