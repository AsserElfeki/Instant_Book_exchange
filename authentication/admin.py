from django.contrib import admin
from .models import BookReader, Notification, ProfileImage

admin.site.register(BookReader)
admin.site.register(ProfileImage)
admin.site.register(Notification)
