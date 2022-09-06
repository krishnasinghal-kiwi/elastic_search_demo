"""Views File."""
import imp
from rest_framework import viewsets
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import  FilteringFilterBackend, CompoundSearchFilterBackend

from news.documents import NewsDocument
from .models import News
from .serializers import NewsListSerializer
# Create your views here.

class NewsListView(viewsets.ModelViewSet):
    """View for Listing of News."""
    
    serializer_class = NewsListSerializer
    queryset = News.objects.all()

class NewsDocumentView(DocumentViewSet):
    """View for Listing of News."""

    document = NewsDocument
    serializer_class = NewsListSerializer
    filter_backends = [FilteringFilterBackend, CompoundSearchFilterBackend]
    search_fields=['title', 'content']
    multi_match_search_fields=['title', 'content']
    filter_fields = {'title':'title','content':'content'}