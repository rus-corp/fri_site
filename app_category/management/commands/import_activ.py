import csv
from typing import Any, Optional

from django.core.management.base import BaseCommand

from app_category.models import Activity

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('activity.csv', 'r') as file:
            activity = list(csv.DictReader(file, delimiter=';'))

        for activ in activity:
            a = Activity(id=activ['id'], name=activ['name'])
            a.save()
        