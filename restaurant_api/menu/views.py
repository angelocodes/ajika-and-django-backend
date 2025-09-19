from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ItemSerializer
from .models import Item

# Create your views here.
"""def item_list(request):
    
     
    #Below, we changes the Django QuerySet to a list of dictionaries
    #QueryObj => Python list[dicts]
    items = Item.objects.all()
    #return render(request, 'menu/item_list.html', {'items': items})
    item_list = []


    for item in items:
        item_list.append(
            {
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'price': item.price,
            }
        )
    return JsonResponse({"menu_items": item_list})  # Convert QuerySet to list if necessary
"""
@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)



# serialization refers to converting complex data types, 
# such as Django QuerySets or model instances, into native Python data types
# that can then be easily rendered into JSON, XML, or other content types. 
# This is particularly useful when building APIs where you need to send data over 
# the web in a format that can be easily consumed
# by clients, such as web browsers or mobile apps.


def item_list_serialized(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    #return JsonResponse(serializer.data, safe=False)  # Use serializer.data to get the serialized data
    return JsonResponse({"menu_items": serializer.data})  # Use serializer.data to get the serialized data

@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
    