from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.caption}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True)
    # related_name is so when querying we don't have to use post_set so we rename it
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'post title: {self.title}'
