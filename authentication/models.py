from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save


class BookReader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        book_reader, created = BookReader.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)
