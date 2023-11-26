import json
from datetime import datetime

import pytest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from book_manager.models import Book
from book_manager.views import BookViewSet
from users.models import User


@pytest.mark.django_db
class TestViews(TestCase):
    factory = RequestFactory()
    client = Client()

    @pytest.fixture(name='added_book')
    def test_create_book(self, room, user):
        """"Создание новой книги"""
        url = reverse('books-list')
        request = self.factory.post(url, data={"name": "Война и мир",
                                               "author": 'Лев Толстой',
                                               "pub_year": 1865,
                                               "isbn": '9780393042375'
                                               })
        response = BookViewSet.as_view({'post': 'create'})(request).render()
        final_resp = json.loads(response.content.decode("utf-8"))
        assert response.status_code == 201
        assert isinstance(final_resp, dict)
        return {'book': final_resp}
