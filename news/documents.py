"""Documents File."""
from django_elasticsearch_dsl import Document, fields, Index
from .models import News

PUBLISHER_INDEX = Index('news_demo')
PUBLISHER_INDEX.settings(
    # See Elasticsearch Indices API reference for available settings
    number_of_shards=1,
    number_of_replicas=1
)

@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
    id = fields.IntegerField(attr='id')
    title = fields.TextField(fields={
        'raw':{'type':'keyword'}
    })
    short_description = fields.TextField(fields={
        'raw':{'type':'keyword'}
    })
    content = fields.TextField(fields={
        'raw':{'type':'keyword'}
    })
    class Django(object):
        model=News