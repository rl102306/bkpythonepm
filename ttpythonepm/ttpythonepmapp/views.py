from contextlib import nullcontext
from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

import requests


class InfoGraficas(APIView):

    def get(self, request):
            
            URL = 'https://sitr.cnd.com.pa/m/pub/data/gen.json'

            data = requests.get(URL) 

            Json_Data = data.json()

           
            if data != '':
               
               return Response(Json_Data,status=200,content_type="application/json")
            
            else:
            
               return Response('Eror',status=400,content_type="text/plain")