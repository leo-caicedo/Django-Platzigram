# Django
from django.contrib import admin

# Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'profile', 'title', 'photo')
    list_display_links = ('pk', 'user',)
    list_editable = ('title', 'photo')
