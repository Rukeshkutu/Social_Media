from django.contrib import admin

# Register your models here.
from post.models import Post, PostAttachment

admin.site.register(Post)
admin.site.register(PostAttachment)