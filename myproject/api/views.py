from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from base.models import Item
from .serializers import ItemSerializer
# from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .decorators import get_item_instance

@api_view(['GET'])
def get_items(request):
    if request.method == 'GET':
        items = Item.objects.all()
        # print(args)
        # print(pk)
        print(Item.objects.get(pk=1).name)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_item(request):

    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@get_item_instance
def get_item_detail(request, instance):
    print(instance)
    if request.method == 'GET':
        serializer = ItemSerializer(instance)
        return Response(serializer.data)

@api_view(['PUT'])
@get_item_instance    
def update_item_detail(request, instance):
    
    if request.method == 'PUT':
        serializer = ItemSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@get_item_instance    
def delete_item(request, instance):

    if request.method == 'DELETE':
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)