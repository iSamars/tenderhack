# Generated by Django 3.2.9 on 2021-11-13 06:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('e314b25c-e41c-44ea-bbba-683243235803'), max_length=255, unique=True),
        ),
    ]
