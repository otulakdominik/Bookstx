from django.contrib import admin

from .models import(
    Book,
    Author,
    Categories,
)


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'publishedDate',
        'averageRating',
        'ratingsCount',
        'imageLink',
    )
    filter_horizontal = ('authors', 'categories',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Book, BookAdmin)