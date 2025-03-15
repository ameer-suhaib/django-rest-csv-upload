from django.shortcuts import render

# Create your views here.

import csv
import io
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

import logging

logger = logging.getLogger(__name__)



@api_view(['GET'])
def test_api(request):
    return Response({"message": "Hello World!"})


@api_view(['POST'])
def upload_csv(request):
    logger.info('Entert to the function')
    if 'file' not in request.FILES:
        return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

    file = request.FILES['file']
    
    if not file.name.endswith('.csv'):
        return Response({"error": "File is not a CSV."}, status=status.HTTP_400_BAD_REQUEST)
    logger.info('Checked file type completed')

    decoded_file = file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    total_saved = 0
    total_rejected = 0
    validation_errors = []

    for row in csv.reader(io_string, delimiter=','):
        name, email, age = row
        user_data = {'name': name, 'email': email, 'age': age}
        serializer = UserSerializer(data=user_data)

        if serializer.is_valid():
            try:
                serializer.save()
                total_saved += 1
            except Exception as e:
                validation_errors.append({"email": email, "error": str(e)})
        else:
            total_rejected += 1
            validation_errors.append({"email": email, "errors": serializer.errors})

    logger.info('Returning response with status code')
    return Response({
        "total_saved": total_saved,
        "total_rejected": total_rejected,
        "validation_errors": validation_errors
    }, status=status.HTTP_200_OK)


