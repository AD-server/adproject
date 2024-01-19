from django.shortcuts import render
import pymysql
from django.db import connection
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from adserver.models import db_connection, db_excute, db_info

db_connecter = db_connection(db_info["host"], db_info["user"], db_info["password"], db_info["db"], db_info["charset"])
db_excuter = db_excute(db_connecter)

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'index.html')

def ad_list(request):
    return render(request, 'ad_list.html')

@csrf_exempt
def add_product(request):
    inputdata = json.loads(request.body.decode('utf-8'))
    advertiser_id = inputdata['advertiser_id']
    title = inputdata['product_name']
    target = inputdata['target']
    sql = f"""insert into product (title, target, advertiser_id) values ('{title}', '{target}', '{advertiser_id}');"""
    data = db_excuter.execute_query(sql)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

@csrf_exempt
def add_ad(request):
    inputdata = json.loads(request.body.decode('utf-8'))
    ad_url = inputdata['ad_url']
    link_url = inputdata['link_url']
    slot_id = inputdata['slot_id']
    cost_type = inputdata['cost_type']
    end_date = inputdata['end_date']
    start_date = inputdata['start_date']
    product_id = inputdata['product_id']
    sql = f"""INSERT INTO ad (url, link_url, slot_id, cost_type, end_date, start_date, product_id) values ('{ad_url}', '{link_url}', '{slot_id}', '{cost_type}', '{end_date}', '{start_date}', '{product_id}');"""
    data = db_excuter.execute_query(sql)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

@csrf_exempt
def detail_ad(request):
    inputdata = json.loads(request.body.decode('utf-8'))
    ad_id = inputdata['ad_id']
    sql = f"""select advertiser_id, title, target, url, link_url, slot_id, cost_type, end_date, start_date from product, ad where product.product_id = ad.product_id and ad_id = {ad_id};"""
    data = db_excuter.execute_query(sql)
    if data == {"success" : False}:
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')
    else:
        return JsonResponse({"ad_id": ad_id, "advertiser_id" : data[0][0], "product_name" : data[0][1], "target" : data[0][2], "url" : data[0][3], "link_url" : data[0][4], "slot_id" : data[0][5], "cost_type" : data[0][6], "end_date" : data[0][7], "start_date" : data[0][8]}, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

@csrf_exempt
def search_ad(request):
    inputdata = json.loads(request.body.decode('utf-8'))
    filter = inputdata['condition']
    input = inputdata['search_input']
    if filter == "ad_id":
        sql = f"""select ad_id, ad.slot_id, start_date, end_date, content_type from ad,slot,product where slot.slot_id = ad.slot_id and product.product_id = ad.product_id and ad_id like "%{input}%" order by ad_id;"""
        data = db_excuter.execute_query(sql)
        if data == {"success" : False}:
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')
        else:
            json_data = {"data": [{"ad_id": ad_id, "slot_id": slot_id, "start_date": start_date, "end_date": end_date, "content_type": content_type} for ad_id, slot_id, start_date, end_date, content_type in data]}
            return JsonResponse(json_data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

    elif filter == "product_name":
        sql = f"""select ad_id, ad.slot_id, start_date, end_date, content_type from ad,slot,product where slot.slot_id = ad.slot_id and product.product_id = ad.product_id and title like "%{input}%" order by ad_id;"""
        data = db_excuter.execute_query(sql)
        print(data)
        if data == {"success" : False}:
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')
        else:
            json_data = {"data": [{"ad_id": ad_id, "slot_id": slot_id, "start_date": start_date, "end_date": end_date, "content_type": content_type} for ad_id, slot_id, start_date, end_date, content_type in data]}
            return JsonResponse(json_data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

@csrf_exempt
def edit_ad(request):
    inputdata = json.loads(request.body.decode('utf-8'))
    ad_id = inputdata['ad_id']
    ad_url = inputdata['ad_url']
    link_url = inputdata['link_url']
    slot_id = inputdata['slot_id']
    cost_type = inputdata['cost_type']
    end_date = inputdata['end_date']
    start_date = inputdata['start_date']
    sql = f"""update ad SET url = '{ad_url}', link_url = '{link_url}', slot_id = {slot_id}, cost_type = '{cost_type}', end_date = '{end_date}', start_date = '{start_date}' where ad_id = {ad_id};"""
    data = db_excuter.execute_query(sql)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

@csrf_exempt
def delete_ad(request):
    inputdata = json.loads(request.body.decode('utf-8'))
    ad_id = inputdata['ad_id']
    sql = f"""delete from ad where ad_id = {ad_id};"""
    data = db_excuter.execute_query(sql)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')

@csrf_exempt
def test_ad(request):
    inputdata = json.loads(request.body.decode('utf-8'))
    product_name = inputdata['product_name']
    sql = f"""select ad.slot_id, url, link_url from ad,slot,product where slot.slot_id = ad.slot_id and product.product_id = ad.product_id and title like "%{product_name}%" ;"""
    data = db_excuter.execute_query(sql)
    if data == {"success" : False}:
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')
    else:
        json_data = {"data": [{"slot_id": slot_id, "ad_url" : ad_url, "link_url" : link_url} for slot_id, ad_url, link_url in data]}
        return JsonResponse(json_data, json_dumps_params={'ensure_ascii': False}, content_type = 'application/json; charest=utf-8')