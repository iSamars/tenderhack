# Generated by Django 3.2.9 on 2021-11-13 09:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('c37c863a-e657-471d-b1ab-dc2dd80c69ae'), max_length=255, unique=True),
        ),
    ]
