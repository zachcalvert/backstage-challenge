import json

from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from api.functions import sum_of_squares, square_of_sums


class SumOfSquaresTestCase(TestCase):
    def test_ten(self):
        assert sum_of_squares(10) == 385

    def test_fifty(self):
        assert sum_of_squares(50) == 42925


class SquareOfSumTestCase(TestCase):
    def test_ten(self):
        assert square_of_sums(10) == 3025

    def test_fifty(self):
        assert square_of_sums(50) == 1625625


class DifferenceTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("difference")

    def test_difference(self):
        url = self.url + "?number=10"

        response = self.client.get(url)
        assert response.status_code == 200

        content = json.loads(response.content)
        assert set(content.keys()) == {'datetime', 'number', 'difference'}
        assert content["difference"] == 2640

    def test_bad_value(self):
        url = self.url + "?number=x"

        response = self.client.get(url)
        assert response.status_code == 400
