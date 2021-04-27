from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    inlines = [ CommentInline, ]


admin.site.register(Post)
admin.site.register(Comment)