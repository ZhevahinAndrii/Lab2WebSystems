from django.http import JsonResponse
from django.shortcuts import render


def product_detail(request, product_id):
    response_data = {
        'id': str(product_id),
        'name': f'{product_id} name'
    }
    return JsonResponse(response_data)
