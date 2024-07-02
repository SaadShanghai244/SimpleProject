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

@api_view(['GET'])
def say_hello(request, name):
    try:
        return JsonResponse(
            {
                "message": f"Hello {name}"
            }
        )
    except Exception as e:
        print("Error message    :   ",e)

@api_view(['GET'])
def say_bye(request, name):
    try:
        print("request.data")
        print(request.data)
        return JsonResponse(
            {
                "message": f"Bye  {name}"
            }
        )
    except Exception as e:
        print("Error message    :   ",e)

