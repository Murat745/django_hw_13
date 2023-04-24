from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    born = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote_text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote_text
