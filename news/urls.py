"""Urls File."""
from django.urls import path, include
from rest_framework import routers

from .views import NewsDocumentView, NewsListView

router = routers.DefaultRouter()
# router.register(r'news', NewsListView)


urlpatterns = [
    # path('', include(router.urls)),
    path('news', NewsDocumentView.as_view({'get':'list'}))

]