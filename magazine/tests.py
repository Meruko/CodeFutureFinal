from django.test import TestCase
from magazine.models import *

# Create your tests here.
class ModelsToStringTestCase(TestCase):
    def test_parametr_to_str(self):
        parametr = Parametr.objects.create(name='TestName')
        self.assertEqual('TestName', str(parametr))

    def test_category_to_str(self):
        category = Category.objects.create(name='TestName')
        self.assertEqual('TestName', str(category))

    def test_tag_to_str(self):
        tag = Tag.objects.create(name='TestName')
        self.assertEqual('TestName', str(tag))