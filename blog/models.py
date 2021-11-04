from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    content = models.TextField()

    def get_absolute_url(self) -> str:
        return reverse("post-detail", args=[self.slug])

    def __str__(self) -> str:
        return self.title
