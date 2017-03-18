from django.contrib import admin

# models
from ubcdataapp.models import Version
from ubcdataapp.models import License
from ubcdataapp.models import Project
from ubcdataapp.models import DNS
from ubcdataapp.models import DWS
from ubcdataapp.models import SO


admin.site.register(Version)
admin.site.register(License)
admin.site.register(DNS)
admin.site.register(DWS)
admin.site.register(SO)
admin.site.register(Project)


