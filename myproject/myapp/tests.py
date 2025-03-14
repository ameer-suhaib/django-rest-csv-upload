from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UserUploadTests(APITestCase):
    def test_upload_valid_csv(self):
        url = reverse('upload_csv')
        print(url,"uuuuuuuuu")
        data = {'file': open('valid_users.csv', 'rb')}
        print(data,"ssssssssss")
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_upload_invalid_csv(self):
        url = reverse('upload_csv')
        data = {'file': open('invalid_users.csv', 'rb')}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)