from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Car, Manufacturer


class DriverModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(
            username="test",
            password="test1234",
            license_number="TST12345"
        )

    def test_driver_str(self):
        driver = get_user_model().objects.get(id=1)
        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )

    def test_get_absolute_url(self):
        driver = get_user_model().objects.get(id=1)
        self.assertEqual(
            driver.get_absolute_url(), "/drivers/1/"
        )


class ManufacturerModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Manufacturer.objects.create(
            name="test_name",
            country="test_country"
        )

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.get(id=1)
        self.assertEqual(
            str(manufacturer),
            f"{manufacturer.name} {manufacturer.country}"
        )


class CarModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        manufacturer = Manufacturer.objects.create(
            name="test_name",
            country="test_country"
        )
        driver = get_user_model().objects.create(
            username="test",
            password="test1234",
            license_number="TST12345"
        )
        car = Car.objects.create(
            model="test_model",
            manufacturer=manufacturer
        )
        car.drivers.add(driver)

    def test_car_str(self):
        car = Car.objects.get(id=1)
        self.assertEqual(str(car), car.model)
