from django.shortcuts import render
import pymysql
from django.db import connection
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def add_product(request):
    # print(request.body)
    inputdata = json.loads(request.body.decode('utf-8'))
    advertiser_id = inputdata['advertiser_id']
    title = inputdata['title']
    target = inputdata['target']
    # print(inputdata)
    try:
        with pymysql.connect(host = "localhost", user = "root", password = "s01010101!", db = 'ad', charset = 'utf8') as conn:

            cursor = conn.cursor()

            sql = f"""INSERT INTO product (title, target, advertiser_id) values ('{title}', '{target}', '{advertiser_id}');"""

            cursor.execute(sql)
            conn.commit()

            return JsonResponse({'success' : True}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')
    except Exception as e:    
        print('예외가 발생했습니다.', e)
        return JsonResponse({'success' : False}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

@csrf_exempt
def add_ad(request):
    # print(request.body)
    inputdata = json.loads(request.body.decode('utf-8'))
    ad_url = inputdata['ad_url']
    link_url = inputdata['link_url']
    slot_id = inputdata['slot_id']
    cost_type = inputdata['cost_type']
    end_date = inputdata['end_date']
    start_date = inputdata['start_date']
    product_id = inputdata['product_id']
    # print(inputdata)
    try:
        with pymysql.connect(host = "localhost", user = "root", password = "s01010101!", db = 'ad', charset = 'utf8') as conn:

            cursor = conn.cursor()

            sql = f"""INSERT INTO ad (url, link_url, slot_id, cost_type, end_date, start_date, product_id) values ('{ad_url}', '{link_url}', '{slot_id}', '{cost_type}', '{end_date}', '{start_date}', '{product_id}');"""

            cursor.execute(sql)
            conn.commit()

            return JsonResponse({'success' : True}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')
    except Exception as e:    
        print('예외가 발생했습니다.', e)
        return JsonResponse({'success' : False}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')
