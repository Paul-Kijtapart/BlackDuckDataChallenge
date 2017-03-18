from django.core.management.base import BaseCommand, CommandError
import csv
from os import path
import ubcdataapp

# absolute path
ORIGINAL_DATA_PATH = path.join(ubcdataapp.__path__[0], "original_data")
SAMPLE_DATA_PATH = path.join(ORIGINAL_DATA_PATH, "sample.csv")

# models
from ubcdataapp.models import Version
from ubcdataapp.models import License
from ubcdataapp.models import Project
from ubcdataapp.models import DNS
from ubcdataapp.models import DWS
from ubcdataapp.models import SO


class Command(BaseCommand):
    help = 'Load Initial CSV data to PostgreSQL database'

    def handle(self, *args, **options):
        with open(SAMPLE_DATA_PATH, "r") as csvfile:
            lines = csv.reader(csvfile, delimiter=';', quotechar='"')
            for line_count in range(5):
                print(lines.__next__())
        self.stdout.write("Successfully Load initial data to PostgreSQL database.")
