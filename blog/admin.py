from django.contrib import admin

from .models import Author, Tag, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'tag')
    list_display = ('title', 'date', 'author')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

class TagAdmin(admin.ModelAdmin):
    list_display = ['caption']

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)