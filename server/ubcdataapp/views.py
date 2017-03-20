from django.shortcuts import render

from django.http import HttpResponse
from ubcdataapp import db_query_helper
from django.core import serializers
from django.http import JsonResponse
from os import path
import ubcdataapp
import json

# models
from ubcdataapp.models import Version
from ubcdataapp.models import License
from ubcdataapp.models import Project
from ubcdataapp.models import DNS
from ubcdataapp.models import DWS
from ubcdataapp.models import SO

# paths
CACHED_DATA_PATH = path.join(path.join(ubcdataapp.__path__[0]), "cached_data")


def index(request):
    return HttpResponse("Hello, you are at ubcdata app apge.")


def projects(request, project_id=None, limit=None):
    res = None
    focus_file = "projects" if not project_id else "project_" + str(project_id)
    focus_file += ".json"
    focus_path =  path.join(CACHED_DATA_PATH, focus_file)
    if not path.isfile(focus_path):
        res = db_query_helper.get_project_with_most_license_querySet()
        res = serializers.serialize("json", res)
        with open(path.join(CACHED_DATA_PATH, "projects.json"), "w") as outfile:
            json.dump(res, outfile, sort_keys=True, indent=4, separators=(',', ': '))
    else:
        with open(path.join(CACHED_DATA_PATH, "projects.json"), 'r') as infile:
            res = json.load(infile)

    return HttpResponse(res, content_type="application/json")


def versions(request, limit=None):
    """
    Get a List of Versions ordered by the number of projects that use it
    :param request:
    :param limit:
    :return:
    """
    res = db_query_helper.get_version_used_by_most_projects_querySet(limit)
    return HttpResponse(
        serializers.serialize("json", res),
        content_type="application/json"
    )


def licenses(request, limit=None):
    """
    Get a List of Licenses ordered by the number of projects that use it
    :param request:
    :param limit: number to return
    :return: json
    """
    res = db_query_helper.get_license_used_by_most_projects_querySet(limit)
    return HttpResponse(
        serializers.serialize("json", res),
        content_type="application/json"
    )
