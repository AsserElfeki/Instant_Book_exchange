from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField, PPOIField
from polymorphic.models import PolymorphicModel


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()
    book = models.ForeignKey('boookzdata.Book', related_name='images', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"id-{self.pk} {self.name}"


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


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ManyToManyField(Author, related_name='books')
    category = models.ManyToManyField(Category, related_name='books')
    condition = models.ForeignKey('boookzdata.BookCondition', related_name='books',on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    book_shelf = models.ForeignKey('boookzdata.BookShelf', on_delete=models.CASCADE, blank=True, null=True, related_name='books', related_query_name='book')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"id-{self.pk} {self.title}"

    def get_book_reader(self):
        return self.book_shelf.book_reader


class BookShelf(PolymorphicModel):
    book_reader = models.ForeignKey('authentication.BookReader', on_delete=models.CASCADE, related_name='book_shelfs', related_query_name='book_shelfs')
    non_polymorphic = models.Manager()

    class Meta():
        base_manager_name = 'non_polymorphic'

    def __str__(self):
        return f"{self.book_reader.user}'s shelf"



class GiveawayBookshelf(BookShelf):
    pass

    def __str__(self):
        return f"{self.book_reader.user}'s give-away shelf"


class WantedBookshelf(BookShelf):
    pass

    def __str__(self):
        return f"{self.book_reader.user}'s wanted shelf"


class BookSite(models.Model):
    name = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    book_condition = models.ForeignKey(BookCondition, on_delete=models.CASCADE, related_name='sites',
                                       related_query_name='site')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    url = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class CustomerReportRecord(models.Model):
    time_raised = models.DateTimeField(default=timezone.now, editable=False)
    reference = models.CharField(unique=True, max_length=20)
    description = models.TextField()
