from django.shortcuts import render
import pymysql
from django.db import connection
from django.http import JsonResponse, HttpResponse
import json


# Create your views here.
def index(request):
    return render(request, 'index.html')


