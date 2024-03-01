from django.shortcuts import render
from rest_framework import generics,filters
from .models import Review
from .serializers import ReviewSerializers
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ReviewList(generics.ListAPIView):
    queryset= Review.objects.order_by('-created_at').all()
    serializer_class= ReviewSerializers
    filter_backends= [DjangoFilterBackend]
    filterset_fields= ['item_id']

class ReviewAdd(generics.CreateAPIView):
    queryset= Review.objects.all()
    serializer_class= ReviewSerializers
    