from rest_framework.test import APITestCase
from rest_framework import status
from shop.models import Product, Category
from api.serializers import ProductSerializer


class ProductApiTestCase(APITestCase):
    def test_get(self):
        category = Category.objects.create(
            name='category'
        )
        product_1 = Product.objects.create(
            name='product_1',
            price=100,
            category=category
        )
        url = f'/api/product/{product_1.pk}/'
        response = self.client.get(url)
        serial_data = ProductSerializer(product_1).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serial_data, response.data)

    def test_get_list(self):
        category = Category.objects.create(
            name='category'
        )
        product_1 = Product.objects.create(
            name='product_1',
            price=100,
            category=category
        )
        product_2 = Product.objects.create(
            name='product_2',
            price=150,
            category=category
        )
        url = '/api/product/'
        response = self.client.get(url)
        serial_data = ProductSerializer([product_1, product_2], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serial_data, response.data)

    def test_post(self):
        category = Category.objects.create(
            pk=10,
            name='category'
        )
        product_1 = Product(
            pk=10,
            name='product_1',
            price=237,
            category=category
        )
        serial_data = ProductSerializer(product_1).data
        url = '/api/product/'

        response = self.client.post(url, data={
            'name': 'product_1',
            'price': 237,
            'category': category.id,
            'exists': True
        })

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(serial_data.get('name'), response.data.get('name'))
        self.assertEqual(serial_data.get('price'), response.data.get('price'))
        self.assertEqual(serial_data.get('category'), response.data.get('category'))
        self.assertEqual(serial_data.get('exists'), response.data.get('exists'))
