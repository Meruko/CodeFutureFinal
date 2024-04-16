from django.test import TestCase
from news.utils import *

class CalculateMoneyDefTestCase(TestCase):
    def test_sum_count_price_pass(self):
        result = sum_price_count(price=100, count=10)
        self.assertEqual(result, 1000)

    def test_sum_count_price_discount_pass(self):
        result = sum_price_count(price=200, count=15, discount=5)
        self.assertEqual(result, 2850)

    def test_sum_count_price_nds_pass(self):
        result = sum_price_count(price=400, count=6, nds=12)
        self.assertEqual(result, 2112)

    def test_sum_count_price_discount_nds_pass(self):
        result = sum_price_count(price=500, count=105, discount=6, nds=12)
        self.assertEqual(43428, result)

class CalculateMoneyClassTestCase(TestCase, CalculateMoney):
    def test_sum_price_count_pass(self):
        result = self.sum_price_count(price=400, count=19)
        self.assertEqual(7600, result)

    def test_sum_price_pass(self):
        list_price = [294, 2000, 6942]
        result = self.sum_price(prices=list_price)
        self.assertEqual(9236, result)

    def test_sum_price_discount_pass(self):
        list_price = [200, 640, 720]
        result = self.sum_price(prices=list_price, discount=10)
        self.assertEqual(result, 1404)

    def test_sum_price_nds_pass(self):
        list_price = [1200, 540, 370, 480]
        result = self.sum_price(prices=list_price, nds=8)
        self.assertEqual(2382.8, result)

    def test_sum_price_discount_nds_pass(self):
        list_price = [90, 110]
        result = self.sum_price(prices=list_price, discount=15, nds=2)
        self.assertEqual(166.6, result)