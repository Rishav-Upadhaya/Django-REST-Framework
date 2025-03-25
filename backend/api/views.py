import json
from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.
# def api_home(request, *args, **kwargs):
#     # print(request.GET)
#     # print(request.POST)
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(body)
#     # print(data['query'])
#     data['params']=dict(request.GET)
#     # data["headers"]=dict(request.headers)
#     # data["content_type"]=request.content_type
#     # print(data["headers"])
#     # print(data["content_type"])
#     print(data)
#     # return JsonResponse({"message":"Hi there, This is Your Django API Project"})
#     return JsonResponse(data)

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     # model_data = Product.objects.filter(title = request.GET["title"])
#     print(model_data)
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title'])
#         # data["id"] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#     return JsonResponse(data)

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)

# # Search by title
# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     try:
#         model_data = Product.objects.filter(title=request.GET["title"])
#         data = ProductSerializer(model_data, many=True).data
#         print(model_data)
#         print(data)
#         if data:
#             return Response(data)
#         return Response({"message": "Not found"}, status=404)
#     except KeyError:
#         return Response({"message": "Title parameter is required"}, status=400)

# @api_view(['POST'])
# def api_home(request, *args, **kwargs):
#     serializer = ProductSerializer(data=request.data)
#     # print("Request Data: " + str(request.data))
#     # print("Serializer: " + str(serializer))
#     if serializer.is_valid(raise_exception=True):
#         # serializer.save()
#         data = serializer.data
#         # print("Data: " + str(serializer.data))
#         # print(data)
#         # return Response(data)
#         return Response(serializer.data)
#     return Response({"error": "Invalid data"}, status=400)

    


