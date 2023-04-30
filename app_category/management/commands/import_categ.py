import csv
from typing import Any, Optional

from django.core.management.base import BaseCommand

from app_category.models import Activity, Categoryes

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('cat.csv', 'r') as file:
            categories = list(csv.DictReader(file, delimiter=';'))

        for cat in categories:
            activ = Activity.objects.filter(pk=cat['activity']).first()
            c = Categoryes(id=cat['id'], name=cat['name'], activity=activ)
            c.save()