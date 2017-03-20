from django.core.management.base import BaseCommand, CommandError

# Debug and presentation
from pprint import pprint

# Database Query functions
from ubcdataapp import db_query_helper


class Command(BaseCommand):
    help = "Report insights"

    def handle(self, *args, **options):
        with open("report.txt", "w") as outfile:
            pprint("Top 5 Version used by most projects \n"
                   + db_query_helper.get_version_used_by_most_projects_querySet(limit=5)
                   .values().__str__(), stream=outfile)

            pprint("Top 5 License used by most projects \n"
                   + db_query_helper.get_license_used_by_most_projects_querySet(limit=5)
                   .values().__str__(), stream=outfile)

            pprint("Top 5 Projects with Highest number of Distinct Properties \n"
                   + db_query_helper.get_project_with_most_properties_querySet(limit=5)
                   .values("id", "num_dws", "num_dns", "num_so").__str__(), stream=outfile)

            pprint("Top 5 Projects with Highest number of License \n"
                   + db_query_helper.get_project_with_most_license_querySet(limit=5)
                   .values("id", "num_license").__str__(), stream=outfile)

            pprint("Version and the number of projects that use it \n"
                   + db_query_helper.get_version_and_its_project_count_list()
                   .values("version_id", "num_project").__str__(), stream=outfile)

            pprint("License_id and the number of projects that use it \n"
                   + db_query_helper.get_license_and_its_project_count_list()
                   .values().__str__(), stream=outfile)

        self.stdout.write("END OF REPORT")
