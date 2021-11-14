from django.db import models
import uuid

class Contract(models.Model):
    """Contracts model"""

    # Fields
    number = models.TextField(verbose_name="Номер контракта", max_length=255, unique=True, default=uuid.uuid4())
    publication_date = models.DateTimeField(verbose_name="Дата публикации КС на ПП", auto_now_add=True)
    conclusion_date = models.DateTimeField(verbose_name="Дата заключения контракта", auto_now_add=True)
    cost = models.DecimalField(verbose_name="Цена контракта", max_digits=12, decimal_places=2)
    customer_inn = models.BigIntegerField(verbose_name="ИНН заказчика", blank=True, default=None, null=True)
    customer_kpp = models.BigIntegerField(verbose_name="КПП заказчика", blank=True, default=None, null=True)
    customer_name = models.TextField(verbose_name="Наименование заказчика", max_length=255)
    provider_inn = models.BigIntegerField(verbose_name="ИНН поставщика", blank=True, default=None, null=True)
    provider_kpp = models.BigIntegerField(verbose_name="КПП поставщика", blank=True, default=None, null=True)
    provider_name = models.TextField(verbose_name="Наименование поставщика", max_length=255, )
    stu = models.JSONField(verbose_name="СТЕ")

    # Methods
    # TODO: Implement methods or remove

class Category(models.Model):
    """Category model"""

    # Fields
    name = models.TextField(verbose_name="Наименование категории", max_length=255, default="")

    # Methods
    # TODO: Imple
    # ment methods or remove

class STU(models.Model):
    """STU model"""

    # Fields
    name = models.TextField(verbose_name="Название СТЕ", max_length=255, null=False, blank=False)
    category = models.ForeignKey(Category,verbose_name="Категория",  null=False, blank=False, on_delete=models.CASCADE)
    code = models.CharField(verbose_name="Код КПГЗ", max_length=25, null=False, blank=False)
    specifications = models.JSONField(verbose_name="Характеристики", null=False, blank=False)

    # Methods
    # TODO: Implement methods or remove

class Order(models.Model):
    """Orders"""

    class Status(models.TextChoices):
        NEW = 'Новая',
        APPROVED = 'Подтверждена',
        DECLINED_BY_PROVIDER = 'Отконена поставщиком',
        ALTERNATIVE = 'Предложена альтернатива',
        ALTERNATIVE_ACCEPTED = 'Альтернатива/замена подтверждена',
        DECLINED_BY_CUSTOMER = 'Отклонена заказчиком'

    #Fields
    customer = models.TextField(verbose_name="Покупатель", null=False, blank=False)
    provider = models.TextField(verbose_name="Поставщик", null=False, blank=False)
    cost = models.DecimalField(verbose_name="Сумма", max_digits=12, decimal_places=2)
    date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
    status = models.CharField(verbose_name="Статус", choices=Status.choices, default=Status.NEW, max_length=35)


    

