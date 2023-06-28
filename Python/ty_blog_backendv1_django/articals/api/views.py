from django.shortcuts import render
from  rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serilizers import BlogPostSerializer
from ..models import BlogPost

# Create your views here.

# the views.py takes a request and sends a response to the frontend
# this code specifies the serilizer_class and queryset 
class BlogViews(ModelViewSet):
    # this sets up a GET request
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')

class BlogDetail(ModelViewSet):
    model = BlogPost

# set up other crud operations here
# the first one should be POST