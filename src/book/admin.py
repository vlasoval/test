from . import models
from django.contrib import admin

# # Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)
