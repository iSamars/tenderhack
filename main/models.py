from django.db import models

class Contract(models.Model):
    """Contracts model"""

    # Fields
    publication_date = models.DateField(auto_now_add=True)
    conclusion_date = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    customer_inn = models.BigIntegerField(max_length=12)
    customer_kpp = models.BigIntegerField(max_length=9)
    customer_name = models.CharField(max_length=255)
    provider_inn = models.BigIntegerField(max_length=12)
    provider_kpp = models.BigIntegerField(max_length=9)
    provider_name = models.CharField(max_length=255)
    stu = models.JSONField()

    # Methods
    # TODO: Implement methods or remove

class Category(models.Model):
    """Category model"""

    # Fields
    name = models.CharField(max_length=255, default="")

    # Methods
    # TODO: Implement methods or remove

class STU(models.Model):
    """STU model"""

    # Fields
    name = models.CharField(max_length=255, null=True, blank=False)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, null=False, blank=False)
    specifications = models.JSONField(null=False, blank=False)

    # Methods
    # TODO: Implement methods or remove
