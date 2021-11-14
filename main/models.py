from django.db import models
import uuid

class Contract(models.Model):
    """Contracts model"""

    # Fields
    number = models.TextField(max_length=255, unique=True, default=uuid.uuid4())
    publication_date = models.DateField(auto_now_add=True)
    conclusion_date = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    customer_inn = models.IntegerField()
    customer_kpp = models.IntegerField()
    customer_name = models.TextField(max_length=255)
    provider_inn = models.IntegerField()
    provider_kpp = models.IntegerField()
    provider_name = models.TextField(max_length=255)
    stu = models.JSONField()

    # Methods
    # TODO: Implement methods or remove

class Category(models.Model):
    """Category model"""

    # Fields
    name = models.TextField(max_length=255, default="")

    # Methods
    # TODO: Implement methods or remove

class STU(models.Model):
    """STU model"""

    # Fields
    name = models.TextField(max_length=255, null=True, blank=False)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    code = models.CharField(max_length=25, null=False, blank=False)
    specifications = models.JSONField(null=False, blank=False)

    # Methods
    # TODO: Implement methods or remove
