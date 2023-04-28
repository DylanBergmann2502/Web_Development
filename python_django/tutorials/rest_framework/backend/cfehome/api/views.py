import json
from django.http import JsonResponse, HttpResponse

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)  # dont use request.POST, rather request.
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save() # * instance has to be saved, dont know why
        # print(instance)
        print(serializer.data)
        return Response(serializer.data)
'''
# GET method
@api_view(['GET'])  # Django Rest Framework (DRF) View
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        # field to limit result
        # not give back sale_price as expected?
        data = ProductSerializer(instance).data
    return Response(data)
'''
'''
# using JsonResponse
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # serialization
        # model instance (model_data) -> turn to a py dict
        # return json to client
        data = model_to_dict(model_data, fields=['id', 'title', 'price']) # field to limit result
    return JsonResponse(data)
'''
'''
# using HttpResponse
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price']) # field to limit result
        # still cant get the response due to the price failing to be fully converted to json
        # => that's why using JsonResponse is better bc it takes care of all for you 
        json_data_str = json.dumps(data) 
    return HttpResponse(json_data_str, headers={"content-type":"application/json"})
    # HttpResponse defaults the content-type to text/html, in order to get json, have to change the content-type
'''
'''
def api_home(request, *args, **kwargs):
    # (request.GET) # url query params
    print(request.POST)

    body = request.body # byte string of json data
    data = {}
    try:
        data = json.loads(body) # string of Json data -> py dict
    except:
        pass
    print(data)

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)
'''