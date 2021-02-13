from django.contrib import admin
from django.test import TestCase

from ..admin import CatAdmin
from ..models import Cat


class TestCatAdmin(TestCase):
    def test_admin_should_be_registered(self):
        assert isinstance(admin.site._registry[Cat], CatAdmin)

    def test_admin_should_set_list_display(self):
        expected = (
            'name',
            'image',
        )
        assert CatAdmin.list_display == expected
