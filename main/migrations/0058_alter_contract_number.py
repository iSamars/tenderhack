# Generated by Django 3.2.9 on 2021-11-13 13:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0057_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('aa900183-dfc5-40bc-bd4a-d7bf8b6c45a4'), max_length=255, unique=True),
        ),
    ]
