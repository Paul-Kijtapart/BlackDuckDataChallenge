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

    def add_version(self, version_name):
        '''
        Create Version with version_name if Not Exist
        :param version_name: TextField
        :return: void
        '''
        Version.objects.get_or_create(pk=version_name)

    def add_license(self, license_id):
        '''
        Create License with license_id if Not Exist
        :param license_id: IntegerField
        :return: void
        '''
        License.objects.get_or_create(pk=int(license_id))

    def add_dws(self, dws_value):
        '''
        Create DWS with dws_value if Not Exist
        :param dws_value: TextField
        :return: void
        '''
        DWS.objects.get_or_create(pk=dws_value)

    def add_dns(self, dns_value):
        '''
        Create DNS with dns_value if Not Exist
        :param dns_value: TextField
        :return: void
        '''
        DNS.objects.get_or_create(pk=dns_value)

    def add_so(self, so_value):
        '''
        Create SO with so_value if Not Exist
        :param so_value: TextField
        :return: void
        '''
        SO.objects.get_or_create(pk=so_value)

    def add_project(self, project_id,
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
        print("Check M2O version : " + str(assigned_version.project_set.all()))

        dws, created = DWS.objects.get_or_create(pk=dws_value)
        project.dws.add(dws)
        print("Check M2M DWS : " + str(project.dws.all()))

        dns, created = DNS.objects.get_or_create(pk=dns_value)
        project.dns.add(dns)
        print("Check M2M DNS : " + str(project.dns.all()))

        so, created = SO.objects.get_or_create(pk=so_value)
        project.so.add(so)
        print("Check M2M SO : " + str(project.so.all()))

        l, created = License.objects.get_or_create(pk=license_id)
        project.license.add(l)
        print("Check M2M license : " + str(project.license.all()))

    def handle(self, *args, **options):
        call_command("reset_database")
        with open(SAMPLE_DATA_PATH, "r") as csvfile:
            lines = csv.DictReader(csvfile, delimiter=';', quotechar='"')
            count = 0
            for line in lines:
                if (count == 15):
                    break
                count += 1
                print("Given Row : " +
                      line["d_r_uuid"], line["dws"], line["dns"], line["so"], line["version"], line["license_id"])
                self.add_version(line["version"])
                self.add_license(line["license_id"])
                self.add_dws(line["dws"])
                self.add_dns(line["dns"])
                self.add_so(line["so"])
                self.add_project(line["d_r_uuid"],
                                 line["dws"], line["dns"], line["so"],
                                 line["version"], line["license_id"])
                print("")

        self.stdout.write("Successfully Load initial data to PostgreSQL database.")
