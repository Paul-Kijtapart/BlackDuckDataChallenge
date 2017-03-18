from django.test import TestCase
from django.db.utils import IntegrityError

# models
from ubcdataapp.models import Version
from ubcdataapp.models import License
from ubcdataapp.models import DWS
from ubcdataapp.models import DNS
from ubcdataapp.models import SO
from ubcdataapp.models import Project


class VersionTestCase(TestCase):
    def setUp(self):
        Version.objects.create(name="v1")
        Version.objects.create(pk="v2")
        Version.objects.create(pk="v3")

    def test_add_versions(self):
        self.assertEqual(Version.objects.count()
                         , 3
                         , "duplicate with same primary key doesn't get re-add")
        Version.objects.get_or_create(pk="v4")
        self.assertEqual(Version.objects.count(), 4,
                         "Insert duplicate wont get add "
                         "and No Error thrown")
        with self.assertRaises(IntegrityError):
            Version.objects.create(name="v1")


class LicenseTestCase(TestCase):
    def setUp(self):
        License.objects.create(id=30)
        License.objects.create(pk=50)
        License.objects.create(pk=-1)

    def test_add_license(self):
        self.assertEqual(License.objects.count()
                         , 3
                         , "duplicate with same pk does NOT get re-add")
        License.objects.get_or_create(pk=-1)
        self.assertEqual(License.objects.count(), 3,
                         "Insert duplicate wont get add "
                         "and No Error thrown")
        with self.assertRaises(IntegrityError):
            License.objects.create(pk=50)


class DWSTestCase(TestCase):
    def setUp(self):
        DWS.objects.create(pk="dws1")
        DWS.objects.create(pk="dws2")
        DWS.objects.create(pk="dw3")

    def test_add_dws(self):
        self.assertEqual(DWS.objects.count()
                         , 3
                         , "duplicate with same pk does NOT get re-add")
        DWS.objects.get_or_create(pk="dws2")
        self.assertEqual(DWS.objects.count(), 3,
                         "Insert duplicate wont get add "
                         "and No Error thrown")

        with self.assertRaises(IntegrityError):
            DWS.objects.create(value="dw3")


class DNSTestCase(TestCase):
    def setUp(self):
        DNS.objects.create(pk="dns1")
        DNS.objects.create(value="dns2")
        DNS.objects.create(pk="dns3")

    def test_add_dns(self):
        self.assertEqual(DNS.objects.count()
                         , 3
                         , "duplicate with same pk does NOT get re-add")
        DNS.objects.get_or_create(pk="dns2")
        self.assertEqual(DNS.objects.count(), 3,
                         "Insert duplicate wont get add "
                         "and No Error thrown")
        with self.assertRaises(IntegrityError):
            DNS.objects.create(value="dns3")


class SOTestCase(TestCase):
    def setUp(self):
        SO.objects.create(pk="so1")
        SO.objects.create(value="so2")
        SO.objects.create(value="so3")

    def test_add_so(self):
        self.assertEqual(SO.objects.count()
                         , 3
                         , "duplicate with same pk does NOT get re-add")
        SO.objects.get_or_create(pk="so3")
        self.assertEqual(SO.objects.count(), 3,
                         "Insert duplicate wont get add "
                         "and No Error thrown")
        with self.assertRaises(IntegrityError):
            SO.objects.create(pk="so2")


# Create your tests here.
class ProjectTestCase(TestCase):
    def setUp(self):
        # Set up distinct versions
        self.v1 = Version.objects.create(name="v1")
        self.v2 = Version.objects.create(name="v2")
        self.v3 = Version.objects.create(pk="v3")

        # Set up distinct license
        self.l1 = License.objects.create(id="30")
        self.l2 = License.objects.create(pk="50")
        self.l3 = License.objects.create(pk="-1")

        # Set up Project's properties
        self.dws1 = DWS.objects.create(pk="dws1")
        self.dws2 = DWS.objects.create(pk="dws2")
        self.dws3 = DWS.objects.create(pk="dws3")

        self.dns1 = DNS.objects.create(pk="dns1")
        self.dns2 = DNS.objects.create(pk="dns2")
        self.dns3 = DNS.objects.create(pk="dns3")

        self.so1 = SO.objects.create(pk="so1")
        self.so2 = SO.objects.create(pk="so2")
        self.so3 = SO.objects.create(pk="so3")

        # Set up distinct projects with Version
        self.p1 = Project.objects.create(id="p1",
                                         version=self.v1)

        self.p2 = Project.objects.create(pk="p2",
                                         version=self.v2)

        self.p3 = Project.objects.create(pk="p3",
                                         version=self.v3)

    def test_many_to_one_version(self):
        self.assertIn(self.p1, self.v1.project_set.all())
        self.assertIn(self.p2, self.v2.project_set.all())
        self.assertIn(self.p3, self.v3.project_set.all())

    def test_many_to_many_license(self):
        self.p1.license.add(self.l1, self.l2, self.l3)
        self.p2.license.add(self.l2, self.l3)
        self.p3.license.add(self.l3)
        with self.assertRaises(IntegrityError):
            self.p2.license.add(self.l2)

    def test_many_to_many_dws(self):
        self.p1.dws.add(self.dws1, self.dws2, self.dws3)
        self.p2.dws.add(self.dws2, self.dws3)
        self.p3.dws.add(self.dws3)

        self.assertEqual(self.p1.dws.count(), 3)
        self.assertEqual(self.p2.dws.count(), 2)
        self.assertEqual(self.p3.dws.count(), 1)

    def test_many_to_many_dns(self):
        self.p1.dns.add(self.dns1, self.dns2, self.dns3)
        self.p2.dns.add(self.dns2, self.dns3)
        self.p3.dns.add(self.dns3)

        self.assertEqual(self.p1.dns.count(), 3)
        self.assertEqual(self.p2.dns.count(), 2)
        self.assertEqual(self.p3.dns.count(), 1)

    def test_many_to_many_so(self):
        self.p1.so.add(self.so1, self.so2, self.so3)
        self.p2.so.add(self.so2, self.so3)
        self.p3.so.add(self.so3)

        self.assertEqual(self.p1.so.count(), 3)
        self.assertEqual(self.p2.so.count(), 2)
        self.assertEqual(self.p3.so.count(), 1)
