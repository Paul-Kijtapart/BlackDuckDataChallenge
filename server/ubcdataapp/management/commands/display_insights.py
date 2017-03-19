from django.core.management.base import BaseCommand, CommandError

# Database Query functions
from ubcdataapp import db_query_helper


class Command(BaseCommand):
    help = "Report insights"

    def handle(self, *args, **options):
        print("Version used by most projects : "
              + db_query_helper.get_version_used_by_most_projects_querySet(limit=1)[0].__str__())

        print("License used by most projects : "
              + db_query_helper.get_license_used_by_most_projects_querySet(limit=1)[0].__str__())

        print("Projects with Highest number of Distinct Properties : "
              + db_query_helper.get_project_with_most_properties_querySet(limit=1)[0].__str__())

        print("Projects with Highest number of License : "
              + db_query_helper.get_project_with_most_license_querySet(limit=1)[0].__str__())

        self.stdout.write("END OF REPORT")
