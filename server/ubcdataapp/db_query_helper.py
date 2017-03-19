from django.db.models import Count

# debugs
from pprint import pprint

# models
from ubcdataapp.models import Version
from ubcdataapp.models import License
from ubcdataapp.models import DWS
from ubcdataapp.models import DNS
from ubcdataapp.models import SO
from ubcdataapp.models import Project


def get_version_used_by_most_projects_querySet():
    res = Version.objects.annotate(num_projects=Count("project")).order_by("-num_projects")
    return res


def get_license_used_by_projects_querySet():
    res = License.objects.annotate(num_projects=Count("project")).order_by("-num_projects")
    return res


def get_projects_with_version_querySet(version_name):
    return Project.objects.filter(version__name__iexact=version_name)


def get_projects_with_license_querySet(license_id):
    return Project.objects.filter(license__id=license_id).order_by("id")  # TODO: recheck order_by


def get_project_with_most_license_querySet(version_name=""):
    """
    Find the projects that depend on so many license
    :param version_name: TextField
    :return:
    """
    res = None
    if version_name:
        res = get_projects_with_version_querySet(version_name)
    else:
        res = Project.objects.all()
    return res.annotate(num_license=Count("license")).order_by("-num_license")
