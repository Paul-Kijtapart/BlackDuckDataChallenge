from django.core.management.base import BaseCommand, CommandError

# models
from ubcdataapp.models import Version
from ubcdataapp.models import License
from ubcdataapp.models import Project
from ubcdataapp.models import DNS
from ubcdataapp.models import DWS
from ubcdataapp.models import SO


class Command(BaseCommand):
    help = 'Delete All rows of All Tables'

    def handle(self, *args, **options):
        Version.objects.all().delete()
        License.objects.all().delete()
        Project.objects.all().delete()
        DNS.objects.all().delete()
        DWS.objects.all().delete()
        SO.objects.all().delete()
        self.stdout.write("Successfully Deleted All rows of all Tables.")
