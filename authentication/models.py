from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

from boookzdata.models import BookWantedShelf, BookGiveawayShelf


class BookReader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s profile"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        book_reader, created = BookReader.objects.get_or_create(user=instance)
        wanted_shelf, created = BookWantedShelf.objects.get_or_create(book_reader=book_reader)
        giveaway_shelf, created = BookGiveawayShelf.objects.get_or_create(book_reader=book_reader)


post_save.connect(create_user_profile, sender=User)
