from __future__ import unicode_literals

from django.db import models


# TODO: Create your models here.

class Version(models.Model):
    name = models.CharField  # TODO: max-len maybe
    pass


class License(models.Model):
    pass


class Dependency(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    pass


class Project(models.Model):
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    pass


class Project_DWS(models.Model):
    pass


class Project_DNS(models.Model):
    pass


class Project_SO(models.Model):
    pass
