from django.db import models


class Author(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)

    def __str__(self):
        return '', self.first_name, ' ', self.last_name


class Book(models.Model):
    title = models.CharField(max_length=255, default=' ')
    description = models.TextField(default=' ')
    author = models.ForeignKey('Author', related_name='book', on_delete=models.CASCADE, default=' ')

    def __str__(self):
        return self.title