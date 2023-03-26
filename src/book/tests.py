from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

# https://www.django-rest-framework.org/api-guide/testing/#api-test-cases


class AuthorTests(APITestCase):
    def test_author_creation(self):
        url = "/api/author/"
        data = {'name': 'Some Author Name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().name, 'Some Author Name')


class BookTests(APITestCase):
    def test_book_creation(self):
        url = "/api/book/"
        data = {
            'title': 'Book Title',
            'author': [{"name": "Author name"}],
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Book Title')

        self.assertEqual(Book.objects.get().author.count(), 1)

