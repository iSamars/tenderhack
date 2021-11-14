# Generated by Django 3.2.9 on 2021-11-13 11:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('05e2c5ad-7a4b-439f-8322-4f67ed8608c2'), max_length=255, unique=True),
        ),
    ]
