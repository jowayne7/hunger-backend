from django.shortcuts import render
from rest_framework import generics,filters
from .serializers import ItemSerializer
from .models import Item
from django_filters.rest_framework import DjangoFilterBackend 

# Create your views here.

class ItemList(generics.ListAPIView):
    queryset= Item.objects.order_by('-created_at').filter(status='active')
    serializer_class=ItemSerializer
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields=['category']
    search_fields=['name']