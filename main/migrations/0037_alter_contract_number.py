# Generated by Django 3.2.9 on 2021-11-13 11:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('93fa96d2-4c1b-43bf-bdd8-b34ffd5953d1'), max_length=255, unique=True),
        ),
    ]
