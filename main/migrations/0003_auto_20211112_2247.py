# Generated by Django 3.2.9 on 2021-11-12 22:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='contract',
            name='customer_name',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('612dc03a-0db5-4855-b281-c16aa25a3fa7'), max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='provider_name',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='stu',
            name='name',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
