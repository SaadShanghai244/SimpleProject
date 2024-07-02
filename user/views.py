# from django.shortcuts import render
from rest_framework.decorators import api_view, schema
from django.http import JsonResponse


@api_view(['GET'])
def check_status(request):
    try:
        
        return JsonResponse(
            {
                "status": "Working"
            }
        )
    except Exception as e:
        print("Error message    :   ",e)

