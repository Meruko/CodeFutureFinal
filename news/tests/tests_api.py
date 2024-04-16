from rest_framework.test import APITestCase
from rest_framework import status
from news.models import NewsBD
from news.serializers import NewsSerializer

class NewsAPITestCase(APITestCase):
    def test_get_list(self):
        news_1 = NewsBD.objects.create(title='Test1', anons='Test1', content='Test1', date='2024-03-01T16:24:00Z')
        news_2 = NewsBD.objects.create(title='Test2', anons='Test2', content='Test2', date='2024-03-01T16:25:00Z')
        serial_data = NewsSerializer([news_1, news_2], many=True).data
        url = '/api/news_vs/'

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serial_data, response.data)

    def test_get(self):
        news = NewsBD.objects.create(title='Test3', anons='Test3', content='Test3', date='2024-03-01T16:41:00Z')
        serial_data = NewsSerializer(news).data
        url = f'/api/news_vs/{news.pk}/'

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serial_data, response.data)

    def test_post(self):
        news = NewsBD(title='Test4', content='Test4', anons='Test4', date='2024-03-01T16:43:00Z')
        serial_data = NewsSerializer(news).data
        url = '/api/news_vs/'

        response = self.client.post(url, data={
            'title': 'Test4',
            'anons': 'Test4',
            'content': 'Test4',
            'date': '2024-03-01T16:43:00Z'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(serial_data.get('title'), response.data.get('title'))
        self.assertEqual(serial_data.get('anons'), response.data.get('anons'))
        self.assertEqual(serial_data.get('content'), response.data.get('content'))
        self.assertEqual(serial_data.get('date'), response.data.get('date'))