from django.core.management.base import BaseCommand, CommandError

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
        self.stdout.write("Successfully Load initial data to PostgreSQL database.")
        pass
