from dataclasses import dataclass
from multiprocessing.spawn import import_main_path
from weakref import ref
from cairo import Status
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from html5lib import serialize
from itsdangerous import Serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from refdb.models import RefDB
from refdb.serializers import RefDbSerializer
# Create your views here.

def refdb_list(request):
    if request.method == 'GET':
        refdb = RefDB.objects.all()
        serialize = RefDbSerializer(refdb, many=True)
        return JsonResponse(serialize.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialize = RefDbSerializer(data=data)
        if serialize.is_valid():
            Serializer.save()
            return JsonResponse(Serializer.data,status=201)
            return JsonResponse(Serializer.errors, status=400)

def refdb_detail(request,pk):
    try:
        refdb = RefDB.objects.get(pk=pk)
        except 
