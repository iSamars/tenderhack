# Generated by Django 3.2.9 on 2021-11-13 14:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('a705a62e-4db2-4b76-a044-79174c121b49'), max_length=255, unique=True),
        ),
    ]
