from django.shortcuts import render
from .models import Post 
from django.http import JsonResponse
from rest_framework import generics
from .seriailzers import PostSerializer
# Create your views here.

class PostList(generics.ListAPIView):
    queryset= Post.objects.order_by('created_at').reverse().all()[:20]
    serializer_class= PostSerializer 


class PostAdd(generics.CreateAPIView):
    queryset= Post.objects.all()
    serializer_class= PostSerializer


class PostDetails(generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset= Post.objects.all()
    serializer_class= PostSerializer


class PostDelete(generics.DestroyAPIView):
    queryset= Post.objects.all()
    serializer_class= PostSerializer 