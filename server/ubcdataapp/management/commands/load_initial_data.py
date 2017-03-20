from django.core.management.base import BaseCommand, CommandError
import csv
from os import path
import ubcdataapp
from django.core.management import call_command

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

    def load_row(self, project_id,
                 dws_value, dns_value, so_value,
                 version_name,
                 license_id):
        '''
        Version with version_name, License with license_id,
        dws with dws_value, dns with dns_value,
        and so with so_value must be saved before Project.
        :param project_id: TextField
        :param dws_value: TextField
        :param dns_value: TextField
        :param so_value: TextField
        :param version_name: TextField
        :param license_id: IntegerField
        :return: void
        '''
        assigned_version, created = Version.objects.get_or_create(pk=version_name)
        project, created = Project.objects.get_or_create(pk=project_id, version=assigned_version)
        # print("Version: " + assigned_version.name)
        # print("Check M2O version : " + str(assigned_version.project_set.all()))

        dws, created = DWS.objects.get_or_create(pk=dws_value)
        project.dws.add(dws)
        # print("Check M2M DWS : " + str(project.dws.all()))

        dns, created = DNS.objects.get_or_create(pk=dns_value)
        project.dns.add(dns)
        # print("Check M2M DNS : " + str(project.dns.all()))

        so, created = SO.objects.get_or_create(pk=so_value)
        project.so.add(so)
        # print("Check M2M SO : " + str(project.so.all()))

        l, created = License.objects.get_or_create(pk=license_id)
        project.license.add(l)
        # print("Check M2M license : " + str(project.license.all()))

    def handle(self, *args, **options):
        call_command("reset_database")
        with open(SAMPLE_DATA_PATH, "r") as csvfile:
            lines = csv.DictReader(csvfile, delimiter=';', quotechar='"')
            for line in lines:
                print("Given Row : " +
                      line["d_r_uuid"], line["dws"], line["dns"], line["so"], line["version"], line["license_id"])

                self.load_row(line["d_r_uuid"],
                              line["dws"], line["dns"], line["so"],
                              line["version"], line["license_id"])
                print("")

        self.stdout.write("Successfully Load initial data to PostgreSQL database.", ending="\n\n")
