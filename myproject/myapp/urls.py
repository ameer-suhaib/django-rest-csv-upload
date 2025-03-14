from django.urls import path
from .views import upload_csv,test_api,post_api

urlpatterns = [
    path('test_api/', test_api, name='test_api'),
    path('upload', upload_csv, name='upload_csv'),
    path('post_api/', post_api, name='post_api'),
]