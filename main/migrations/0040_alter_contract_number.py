# Generated by Django 3.2.9 on 2021-11-13 11:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('ac7e9e54-7752-4ea8-8d4a-481d5c394855'), max_length=255, unique=True),
        ),
    ]
