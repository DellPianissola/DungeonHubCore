# Generated by Django 5.1.4 on 2025-01-29 00:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField()),
                ('damage', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'weapon',
            },
        ),
    ]
