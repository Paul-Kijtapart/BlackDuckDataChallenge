from django.core.management.base import BaseCommand, CommandError

# Database Query functions
from ubcdataapp import db_query_helper

class Command(BaseCommand):
    help = "Report insights"

    def handle(self, *args, **options):
        pass
