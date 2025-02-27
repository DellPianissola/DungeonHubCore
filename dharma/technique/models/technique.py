import uuid

from django.db import models


class Technique(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    xp_cost = models.IntegerField()
    type = models.CharField(max_length=50)
    requirements = models.CharField(max_length=100)
    effect = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='technique/', null=True, blank=True)

    def __str__(self):
        return self.id
