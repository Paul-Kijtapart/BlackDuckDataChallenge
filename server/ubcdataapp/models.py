from __future__ import unicode_literals

from django.db import models


class Version(models.Model):
    name = models.TextField(primary_key=True)

    def __str__(self):
        return "name : %s " % (self.name)


class License(models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return "id : %d " % self.id


class DWS(models.Model):
    value = models.TextField(primary_key=True)

    def __str__(self):
        return "value : %s " % (self.value)


class DNS(models.Model):
    value = models.TextField(primary_key=True)

    def __str__(self):
        return "value : %s " % (self.value)


class SO(models.Model):
    value = models.TextField(primary_key=True)

    def __str__(self):
        return "value : %s " % (self.value)


class Project(models.Model):
    id = models.TextField(primary_key=True)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)

    license = models.ManyToManyField(License)
    dws = models.ManyToManyField(DWS)
    dns = models.ManyToManyField(DNS)
    so = models.ManyToManyField(SO)

    def __str__(self):
        return "id : %s" % (self.id)

    def get_license_count(self):
        return self.license.count()

    def get_dws_count(self):
        return self.dws.count()

    class Meta:
        ordering = ("id",)
