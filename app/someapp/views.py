from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import TestModel
import json
import redis
import time

redis_cli = redis.Redis(host='127.0.0.1', port=6379, db=0)

@csrf_exempt
def save_to_redis(request):
    data = json.loads(request.body.decode())
    for key, value in data.items():
        redis_cli.rpush(key, value)
    return JsonResponse({'success': True, 'data': 'Saved in Redis'})

@csrf_exempt
def endpoint(request):
    time.sleep(0.1)
    return JsonResponse({'success': True, 'data': 'Request processed'})

@csrf_exempt
def write_to_db(request):
    data = json.loads(request.body.decode())
    for row in data:
        TestModel.objects.create(key1=row['key1'],
                                 key2=row['key2'],
                                 key3=row['key3'],
                                 key4=row['key4'])
    return JsonResponse({'success': True, 'data': 'Data has been saved'})


