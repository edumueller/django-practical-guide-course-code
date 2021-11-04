from django.db import models
from django.urls import reverse


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "Tags"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name_plural = "Authors"


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="posts")
    content = models.TextField()
    tags = models.ManyToManyField(Tag, null=False)

    def get_absolute_url(self) -> str:
        return reverse("post-detail", args=[self.slug])

    def __str__(self) -> str:
        return self.title
