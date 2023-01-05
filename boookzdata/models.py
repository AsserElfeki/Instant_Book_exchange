from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField, PPOIField


class Image(models.Model):
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()
    book = models.ForeignKey('boookzdata.Book', related_name='images', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.pk}"


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookCondition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookShelf(models.Model):
    shelf_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.shelf_name} shelf"


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ManyToManyField(Author, related_name='books')
    category = models.ManyToManyField(Category, related_name='books')
    language = models.CharField(max_length=255, default="English")
    condition = models.ForeignKey('boookzdata.BookCondition', related_name='books', on_delete=models.CASCADE,
                                  blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    book_reader = models.ForeignKey("authentication.BookReader", on_delete=models.CASCADE, blank=True, null=True,
                                    related_name='book', related_query_name='book')
    book_shelf = models.ForeignKey('boookzdata.BookShelf', on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='book', related_query_name='book')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"id-{self.pk} {self.title}"

    def get_book_reader(self):
        return self.book_reader


class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class ReportRecord(models.Model):
    message = models.CharField(max_length=255)
    book_reader = models.ForeignKey("authentication.BookReader", on_delete=models.CASCADE, related_name='report',
                                    related_query_name='report')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"id-{self.pk} {self.book_reader}'s report"
