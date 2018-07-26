from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloAPIView(APIView):
    """This class model APIView"""

    def get(self, request, format=None):
        """Returns a list of computer programming languages."""
        the_list = [
            'python programming',
            'JAva',
            'perl',
            'php',
            'GO',
            'JS',
            'Swift'
        ]

        return Response({"These are the programming languages i have":the_list})