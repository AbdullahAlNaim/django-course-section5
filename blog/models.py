from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

class Tag(models.Model):
    caption = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    image_name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag)
    post_date = models.DateField(auto_now=True)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)

    def __str__(self):
        return f'post title: {self.title}'
