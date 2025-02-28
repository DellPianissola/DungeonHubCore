import uuid

from django.db import models


class Weapon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    damage = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='weapon/', null=True, blank=True)

    def __str__(self):
        return self.id
