from django.db import models

class Book(models.Model):
    title=models.CharField(
        max_length=40,
        verbose_name='Название книги'   
    )   
    author=models.ManyToManyField(
        'Author',
        verbose_name='Автор',
    )

class Author(models.Model):
    name= models.CharField(
        max_length=40,
        verbose_name='Автор'
        )