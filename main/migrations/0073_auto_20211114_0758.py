# Generated by Django 3.2.9 on 2021-11-14 00:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0072_alter_contract_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(default='', max_length=255, verbose_name='Наименование категории'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='conclusion_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата заключения контракта'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена контракта'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='customer_inn',
            field=models.BigIntegerField(blank=True, default=None, null=True, verbose_name='ИНН заказчика'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='customer_kpp',
            field=models.BigIntegerField(blank=True, default=None, null=True, verbose_name='КПП заказчика'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='customer_name',
            field=models.TextField(max_length=255, verbose_name='Наименование заказчика'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.TextField(default=uuid.UUID('0278f31a-209c-4a00-b2e1-fc2de80a323f'), max_length=255, unique=True, verbose_name='Номер контракта'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='provider_inn',
            field=models.BigIntegerField(blank=True, default=None, null=True, verbose_name='ИНН поставщика'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='provider_kpp',
            field=models.BigIntegerField(blank=True, default=None, null=True, verbose_name='КПП поставщика'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='provider_name',
            field=models.TextField(max_length=255, verbose_name='Наименование поставщика'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации КС на ПП'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='stu',
            field=models.JSONField(verbose_name='СТЕ'),
        ),
        migrations.AlterField(
            model_name='stu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='stu',
            name='code',
            field=models.CharField(max_length=25, verbose_name='Код КПГЗ'),
        ),
        migrations.AlterField(
            model_name='stu',
            name='name',
            field=models.TextField(max_length=255, null=True, verbose_name='Название СТЕ'),
        ),
        migrations.AlterField(
            model_name='stu',
            name='specifications',
            field=models.JSONField(verbose_name='Характеристики'),
        ),
    ]
