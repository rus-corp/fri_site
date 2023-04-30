import csv
from typing import Any, Optional

from django.core.management.base import BaseCommand

from app_category.models import Activity, Categoryes, Specialization

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('spec.csv', 'r') as file:
            specializations = list(csv.DictReader(file, delimiter=';'))

        for spec in specializations:
            categ = Categoryes.objects.filter(pk=spec['category']).first()
            c = Specialization(id=spec['id'], name=spec['specialization'], category=categ)
            c.save()