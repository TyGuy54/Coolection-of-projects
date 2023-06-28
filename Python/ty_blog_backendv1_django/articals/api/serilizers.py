from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = (
        'title',
        'slug',
        'updated_on',
        'content',
        'created_on',
        'status',
        )