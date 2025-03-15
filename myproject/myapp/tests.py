from django.urls import reverse
from rest_framework import status
from django.test import TestCase  # Add this line
import os

class UserUploadTests(TestCase):
    def test_upload_valid_csv(self):
        url = reverse('upload_csv')
        file_path = os.path.join(os.path.dirname(__file__), 'upload', 'valid_users.csv')
        data = {'file': open(file_path, 'rb')}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_upload_invalid_csv(self):
        url = reverse('upload_csv')
        file_path = os.path.join(os.path.dirname(__file__), 'upload', 'invalid_users.csv')
        data = {'file': open(file_path, 'rb')}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)