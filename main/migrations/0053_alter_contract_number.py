# Generated by Django 3.2.9 on 2021-11-13 12:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('11512589-91a9-45e9-a4f9-dccc89200dc1'), max_length=255, unique=True),
        ),
    ]
