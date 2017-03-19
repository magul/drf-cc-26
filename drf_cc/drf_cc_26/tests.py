from __future__ import unicode_literals

from StringIO import StringIO


from rest_framework.test import APITestCase
from djangorestframework_camel_case import parser

from drf_cc_26 import models


class DrfCc26TestCase(APITestCase):

    def setUp(self):
        instance = models.DrfCc26Model(abc_def=True)
        instance.save()

    def test_list_data(self):
        response = self.client.get('/api/drf-cc-26/')
        self.assertIsInstance(response.data[0].pop('abc_def'), bool)

    def test_list_content(self):
        response = self.client.get('/api/drf-cc-26/')
        parsed_content = parser.CamelCaseJSONParser().parse(
            StringIO(response.content))
        self.assertIsInstance(parsed_content[0].pop('abc_def'), bool)

    def test_retrieve_data(self):
        response = self.client.get('/api/drf-cc-26/1/')
        self.assertIsInstance(response.data.pop('abc_def'), bool)

    def test_retrieve_content(self):
        response = self.client.get('/api/drf-cc-26/1/')
        parsed_content = parser.CamelCaseJSONParser().parse(
            StringIO(response.content))
        self.assertIsInstance(parsed_content.pop('abc_def'), bool)
