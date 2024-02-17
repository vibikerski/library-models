from django.db import models

class LibraryBook(models.Model):
    title = models.CharField(max_length=511)
    author = models.CharField(max_length=511)
    isbn = models.CharField(max_length=255, primary_key=True)
    available = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["author"]
        unique_together = (("title", "author"), )