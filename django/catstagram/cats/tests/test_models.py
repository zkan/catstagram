from django.test import TestCase

from ..models import Cat


class TestCat(TestCase):
    def test_cat_should_have_defined_fields(self):
        cat = Cat.objects.create(name='Salee')
        assert cat.name == 'Salee'
