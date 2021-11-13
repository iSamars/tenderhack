import csv

from tenderhack.wsgi import *
from .models import Contract, Category, STU

def read_csv(file):
    Category.objects.all().delete()
    print("Cleared1")
    reader = csv.DictReader(file, delimiter=';')
    cats = []

    for row in reader:
        cats.append(row["Категория"])

    cats = list(set(cats))

    for cat in cats:
        Category(name=cat).save()
    
    print("Completed")
