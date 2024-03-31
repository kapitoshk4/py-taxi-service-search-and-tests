from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Driver, Manufacturer, Car

DRIVER_URL = reverse("taxi:driver-list")
CAR_URL = reverse("taxi:car-list")
MANUFACTURER_URL = reverse("taxi:manufacturer-list")
INDEX_URL = reverse("taxi:index")


class PublicTest(TestCase):
    def test_driver_login_required(self):
        res = self.client.get(DRIVER_URL)
        self.assertNotEquals(res.status_code, 200)

    def test_car_login_required(self):
        res = self.client.get(CAR_URL)
        self.assertNotEquals(res.status_code, 200)

    def test_manufacturer_login_required(self):
        res = self.client.get(MANUFACTURER_URL)
        self.assertNotEquals(res.status_code, 200)

    def test_index_login_required(self):
        res = self.client.get(INDEX_URL)
        self.assertNotEquals(res.status_code, 200)

    def driver_login_required(self):
        res = self.client.get(DRIVER_URL)
        self.assertNotEquals(res.status_code, 200)


class PrivateTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test1",
            password="test1234",
        )
        self.client.force_login(self.user)

    def test_retrieve_drivers(self) -> None:
        get_user_model().objects.create_user(
            username="test123",
            password="test1234",
            license_number="TST12345",
        )
        get_user_model().objects.create_user(
            username="test1234",
            password="test1234",
            license_number="TST12346",
        )
        drivers = get_user_model().objects.all()
        response = self.client.get(DRIVER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["driver_list"]), list(drivers))
        self.assertTemplateUsed(response, "taxi/driver_list.html")

    def test_retrive_cars(self):
        manufacturer = Manufacturer.objects.create(
            name="test",
            country="Test"
        )
        Car.objects.create(
            model="test1",
            manufacturer=manufacturer
        )
        Car.objects.create(
            model="test2",
            manufacturer=manufacturer
        )
        cars = Car.objects.all()
        response = self.client.get(CAR_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["car_list"]), list(cars))
        self.assertTemplateUsed(response, "taxi/car_list.html")

    def test_retrive_manufacturer(self):
        Manufacturer.objects.create(
            name="test1",
            country="Test1"
        )
        Manufacturer.objects.create(
            name="test2",
            country="Test2"
        )
        manufacturers = Manufacturer.objects.all()
        response = self.client.get(MANUFACTURER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["manufacturer_list"]),
            list(manufacturers)
        )
        self.assertTemplateUsed(response, "taxi/manufacturer_list.html")
