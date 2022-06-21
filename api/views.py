from xmlrpc.client import FastParser
from django.shortcuts import render, HttpResponse
from tickets.models import Ariza
from . serializers import ArizaSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# get all ariza


@csrf_exempt
def ariza_list(request):
    if request.method == 'GET':
        arizalar = Ariza.objects.all()
        serializer = ArizaSerializer(arizalar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArizaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
