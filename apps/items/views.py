from rest_framework import generics
from .serializers import ItemSerializers
from django.http import JsonResponse
from. models import Item


class ItemList(generics.ListAPIView):

    queryset = Item.objects.order_by('created_at').reverse().filter(status='active')
    serializer_class = ItemSerializers


