from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.forms import (
    CarSearchForm,
    DriverCreationForm,
    DriverSearchForm,
    DriverLicenseUpdateForm,
    ManufacturerSearchForm
)


class FormTests(TestCase):
    def setUp(self):
        self.test_user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password",
        )

    def test_driver_creation_form(self):
        form = DriverCreationForm(
            data={
                "username": "unique_username",
                "password1": "strong_password123",
                "password2": "strong_password123",
                "license_number": "TST14352",
                "first_name": "test_first",
                "last_name": "test_last"
            }
        )
        self.assertTrue(form.is_valid())

    def test_driver_search_form(self):
        form = DriverSearchForm(
            data={
                "username": "unique_username"
            }
        )
        self.assertTrue(form.is_valid())

    def test_driver_license_update_form(self):
        form = DriverLicenseUpdateForm(
            data={
                "license_number": "TST13451"
            }
        )
        self.assertTrue(form.is_valid())

    def test_car_search_form(self):
        form = CarSearchForm(
            data={
                "model": "test"
            }
        )
        self.assertTrue(form.is_valid())

    def test_manufacturer_search_form(self):
        form = ManufacturerSearchForm(
            data={
                "name": "Test"
            }
        )
        self.assertTrue(form.is_valid())
