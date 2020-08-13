from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(
        _('author'),
        max_length=300,
    )

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(
        _('type'),
        max_length=200,
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        _('title'),
        max_length=200,
    )

    publishedDate = models.DateField(
        _('published Date'),
    )

    averageRating = models.SmallIntegerField(
        _('average rating'),
        blank=True,
    )

    ratingsCount = models.SmallIntegerField(
        _('ratings count'),
        blank=True,
    )

    imageLink = models.URLField(
        _('image link'),
        max_length=300,
        blank=True,
    )

    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Categories)

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')

    def __str__(self):
        return self.title
