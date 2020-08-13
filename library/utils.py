from typing import Union

from .models import (
    Book,
    Author,
    Categories,
)

import re
import requests
import datetime



def fetch_book(title: str) -> Union[None, dict]:
    google_books = requests.get(url='https://www.googleapis.com/books/v1/volumes?q={title}'.format(title=title,))
    books_json = google_books.json()
    bookshelf = books_json['items']

    for book in bookshelf:
        if 'imageLinks' in book['volumeInfo']:
            links = book['volumeInfo']['imageLinks']
        else:
            links['thumbnail'] = 'http://none'

        if 'publishedDate' in book['volumeInfo']:
            date = book['volumeInfo']['publishedDate']

            m = re.match(r'(\d\d\d\d)(?:-(\d\d)-(\d\d))?', date)
            m = m.groups('1')
            fulldate = datetime.date(int(m[0]), int(m[1]), int(m[2]))
        else:
            fulldate = '1111-01-01'
        author_ex = True
        id_authors = []
        if 'authors' in book['volumeInfo']:
            for author in book['volumeInfo']['authors']:
                obj, _ = Author.objects.get_or_create(
                    name=author
                )
                id_authors.append(obj)
        else:
            author_ex = False

        categories_ex = True
        id_categories = []
        if 'categories' in book['volumeInfo']:
            for category in book['volumeInfo']['categories']:
                obj, _ = Categories.objects.get_or_create(
                    name=category,
                )
            id_categories.append(obj)
        else:
            categories_ex = False

        if 'averageRating' not in book['volumeInfo']:
            book['volumeInfo']['averageRating'] = 0

        if 'ratingsCount' not in book['volumeInfo']:
            book['volumeInfo']['ratingsCount'] = 0

        book, _ = Book.objects.get_or_create(
            title=book['volumeInfo']['title'],
            publishedDate=fulldate,
            averageRating=book['volumeInfo']['averageRating'],
            ratingsCount=book['volumeInfo']['ratingsCount'],
            imageLink=links['thumbnail']
        )
        if author_ex == True:
            book.authors.set(id_authors)
        if categories_ex == True:
            book.categories.set(id_categories)
        book.save()

