# Generated by Django 3.2.9 on 2021-11-14 02:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0073_auto_20211114_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('d78aa6b8-715f-4f57-a669-2f177a0490a5'), max_length=255, unique=True, verbose_name='Номер контракта'),
        ),
    ]
