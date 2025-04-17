from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class MyDataViewTest(TestCase):
    def test_get_data(self):
        
        url = reverse('api_data')

        
        response = self.client.get(url)

        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

       
        self.assertEqual(response.data, {'message': 'Hello, world!'})
