import csv

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

def test():
    a = STU.objects.all()
    print(a[0].name)
