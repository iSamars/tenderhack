import csv
import django

from tenderhack.wsgi import *
from .models import Contract, Category, STU

def parse_category(file):
    Category.objects.all().delete()
    print("Cleared categories")
    reader = csv.DictReader(file, delimiter=';')
    cats = []

    for row in reader:
        cats.append(row["Категория"])

    cats = list(set(cats))

    for cat in cats:
        Category(name=cat).save()
    
    print("Completed categories parsing")

def parse_stu(file):
    STU.objects.all().delete()
    print("Cleared STU")
    reader = csv.DictReader(file, delimiter=';')

    for row in reader:
        STU(id = int(row["\ufeffID СТЕ"]), name = row["Название СТЕ"], category=Category.objects.get(name=row["Категория"]), code = row["Код КПГЗ"], specifications = row["Характеристики"]).save()
    
    print("Completed STU parsing")

def parse_contracts(file):
    Contract.objects.all().delete()
    print("Cleared Contracts")
    reader = csv.DictReader(file, delimiter=';')

    for row in reader:
        if row["КПП поставщика"] == '':
            row["КПП поставщика"] = None
        try:
            Contract.objects.update_or_create(number = row["\ufeffНомер контракта"], publication_date = row["Дата публикации КС на ПП"], conclusion_date = row["Дата заключения контракта"], cost = row["Цена контракта"], customer_inn = row["ИНН заказчика"], customer_kpp = row["КПП заказчика"], customer_name = row["Наименование заказчика"], provider_inn = row["ИНН поставщика"], provider_kpp = row["КПП поставщика"], provider_name = row["Наименование поставщика"], stu = row["СТЕ"])
        except django.db.utils.IntegrityError:
            print("Exists!")
    
    print("Completed contructs parsing")
