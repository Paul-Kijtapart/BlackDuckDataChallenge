from django.db.models import Count, F

# debugs
from pprint import pprint

# models
from ubcdataapp.models import Version
from ubcdataapp.models import License
from ubcdataapp.models import Project


def get_version_used_by_most_projects_querySet(limit=None):
    res = Version.objects \
        .annotate(num_projects=Count("project")) \
        .order_by("-num_projects")
    return res if not limit else res[:limit]


def get_version_and_its_project_count_list(limit=None):
    res = Project.objects.values('version') \
        .annotate(num_project=Count("id")) \
        .order_by("-num_project")
    return res if not limit else res[:limit]


def get_license_used_by_most_projects_querySet(limit=None):
    res = License.objects \
        .annotate(num_projects=Count("project", distinct=True)) \
        .order_by("-num_projects")
    return res if not limit else res[:limit]


def get_license_and_its_project_count_list(limit=None):
    res = License.objects\
        .annotate(num_project=Count("project__id")) \
        .order_by("-num_project")
    return res if not limit else res[:limit]


def get_project_with_version_querySet(version_name):
    return Project.objects \
        .filter(version__name__iexact=version_name)


def get_project_with_license_querySet(license_id):
    return Project.objects \
        .filter(license__id=license_id).order_by("id")


def get_project_with_most_properties_querySet(limit=None):
    '''
    Return a querySet of projects who has the highest number of distinct property
    :param limit: k top projects
    :return: none
    '''
    res = Project.objects \
        .annotate(num_dws=Count("dws__value", distinct=True)) \
        .annotate(num_dns=Count("dns__value", distinct=True)) \
        .annotate(num_so=Count("so__value", distinct=True))

    res = res.annotate(num_property=(F("num_dws") + F("num_dns") + F("num_so"))).order_by("-num_property")
    return res if not limit else res[:limit]


def get_project_with_most_license_querySet(version_name=None, limit=None):
    """
    Find the projects that depend on so many license
    :param version_name: TextField
    :return:
    """
    res = None
    if version_name:
        res = get_project_with_version_querySet(version_name)
    else:
        res = Project.objects.all()
    res = res \
        .annotate(num_license=Count("license")) \
        .order_by("-num_license")

    return res if not limit else res[:limit]
