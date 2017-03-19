from __future__ import unicode_literals

from rest_framework import viewsets

from drf_cc_26 import models
from drf_cc_26 import serializers


class DrfCc26ViewSet(viewsets.ModelViewSet):

    """REST API offers' viewset."""

    serializer_class = serializers.DrfCc26Serializer
    queryset = models.DrfCc26Model.objects.all()
