"""Serializers File."""
from dataclasses import fields
from rest_framework import serializers

from news.models import News
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import NewsDocument


class NewsListSerializer(DocumentSerializer):
    """News List Serializer."""

    class Meta:
        model = News
        document = NewsDocument
        fields = ["id","title","short_description","content"]
    
    def get_location(self,obj):
        try:
            return obj.location.to_dict()
        except:
            return {}