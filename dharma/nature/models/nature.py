import uuid

from django.db import models


class Nature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    points = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='nature/')

    def __str__(self):
        return self.id
