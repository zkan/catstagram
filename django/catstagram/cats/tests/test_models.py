import os
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase

from ..models import Cat


class TestCat(TestCase):
    def test_cat_should_have_defined_fields(self):
        name = 'Salee'
        image_mock = MagicMock(spec=File)
        image_mock.name = 'test.png'

        cat = Cat.objects.create(name=name, image=image_mock)

        assert cat.name == 'Salee'
        assert cat.image.name == image_mock.name

        os.remove(f'media/{image_mock.name}')
