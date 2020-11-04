"""Test views in pur_beurre app"""
from django.test import Client

from pytest import mark

from food_substitute.models import Question, Choice

import pdb

@mark.django_db
def test_detail_product():

    client = Client()
    response = client.get("/food_substitute/1")
    # quest = response.context["question"]

    # assert quest.question_text == "What's new"
    assert response.status_code == 301
    # assert response.templates.name == "food_substitute/detail.html"

@mark.django_db
def test_index():

    client = Client()
    response = client.get("/food_substitute/")

    assert response.status_code == 200
    # assert response.templates.name == "food_substitute/index.html"
