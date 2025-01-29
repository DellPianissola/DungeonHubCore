import uuid

from django.db import models


class Weapon(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField()
    damage = models.IntegerField()
    description = models.TextField()
    # image = models.ImageField()

    class Meta:
        db_table = 'weapon'