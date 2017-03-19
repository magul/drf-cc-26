from __future__ import unicode_literals

from django.conf.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from drf_cc_26 import views


router = DefaultRouter()
router.register(r'drf-cc-26', views.DrfCc26ViewSet, base_name='drf-cc-26')


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
