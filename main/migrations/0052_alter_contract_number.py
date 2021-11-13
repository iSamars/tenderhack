# Generated by Django 3.2.9 on 2021-11-13 12:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('b7d033a7-3302-496d-8a34-264630f2371d'), max_length=255, unique=True),
        ),
    ]
