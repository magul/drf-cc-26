from __future__ import unicode_literals

from rest_framework import serializers

from drf_cc_26 import models


class DrfCc26Serializer(serializers.ModelSerializer):

    class Meta:
        model = models.DrfCc26Model
        fields = (
            'abc_def',
        )
