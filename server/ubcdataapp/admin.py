from django.contrib import admin

# Register your models here.

from .models import Version
from .models import License

admin.site.register(Version, License)
