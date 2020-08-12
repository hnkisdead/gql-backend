# coding=utf-8
# future
from __future__ import absolute_import, print_function, unicode_literals

import os

import pytest
from graphene.test import Client
from snapshottest.module import SnapshotTest

from tablet.schema import schema
from tablet.tests.factories import ProductFactory

pytestmark = pytest.mark.django_db

cwd = os.getcwd()


@pytest.fixture
def client():
    return Client(schema)


def get_query(name):
    cwd = os.path.dirname(os.path.realpath(__file__))

    with open(cwd + "/queries/" + name) as f:
        return f.read()


def test_empty(client, snapshot):
    # type: (Client, SnapshotTest) -> None
    query = get_query("resolve_products.graphql")
    result = client.execute(query, variables={"page": 1, "perPage": 10})

    assert "errors" not in result
    snapshot.assert_match(result["data"], "empty")


def test_non_empty(client, snapshot):
    # type: (Client, SnapshotTest) -> None
    query = get_query("resolve_products.graphql")

    ProductFactory(name="Гавайская", category="Пицца")

    result = client.execute(query, variables={"page": 1, "perPage": 10})

    assert "errors" not in result
    snapshot.assert_match(result["data"], "non empty")
