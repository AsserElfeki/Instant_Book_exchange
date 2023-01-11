from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from versatileimagefield.fields import VersatileImageField, PPOIField
from django_countries.fields import CountryField

class BookReader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    languages = models.TextField(null=True, blank=True)
    country = CountryField(blank=True, null=True, default='PL')

    def __str__(self):
        return f"{self.user}'s profile"

class ProfileImage(models.Model):
    image = VersatileImageField(
        'ProfileImage',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()
    book_reader = models.ForeignKey(BookReader, related_name="profile_image", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.pk}"

class Notification(models.Model):
    content = models.TextField()
    book_reader = models.ForeignKey(BookReader, related_name='notification', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    origin = models.TextField()

    def __str__(self):
        return f"{self.pk} {self.book_reader}"

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        book_reader, created = BookReader.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
