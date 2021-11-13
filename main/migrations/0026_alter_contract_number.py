# Generated by Django 3.2.9 on 2021-11-13 07:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('134f2947-f88a-455f-82dc-8ffd7d53cc3d'), max_length=255, unique=True),
        ),
    ]
