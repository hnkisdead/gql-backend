# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import pytest

from tablet.schema.products.mutations.create_product import CreateProductPayload
from tablet.services import product_services

pytestmark = pytest.mark.django_db


def test_ok():
    product = product_services.create_product(CreateProductPayload(name="Пеперони", category="Пицца"))

    assert product is not None


def test_error():
    product_services.create_product(CreateProductPayload(name="Пеперони", category="Пицца"))

    with pytest.raises(Exception):
        product_services.create_product(CreateProductPayload(name="Пеперони", category="Пицца"))
