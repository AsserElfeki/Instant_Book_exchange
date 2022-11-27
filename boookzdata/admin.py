from django.contrib import admin
from .models import Book, Category, Author, BookCondition, BookSite, Comment, Image
from django.contrib.auth.models import Group

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content', )
    list_filter = ('category', )


admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(BookCondition)
admin.site.register(BookSite)
admin.site.register(Comment)

admin.site.unregister(Group)

admin.site.site_header = 'Boookz Admin Panel'
