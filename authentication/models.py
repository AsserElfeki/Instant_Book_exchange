from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from versatileimagefield.fields import VersatileImageField, PPOIField
from django_countries.fields import CountryField

class ProfileImage(models.Model):
    image = VersatileImageField(
        'ProfileImage',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return f"{self.pk}"


class BookReader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.OneToOneField(
        ProfileImage, on_delete=models.CASCADE, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    country = CountryField(blank=True, null=True, default='PL')

    # rating
    # transaction_history

    def __str__(self):
        return f"{self.user}'s profile"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        book_reader, created = BookReader.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
