from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'course', 'title', 'date_posted']
    list_filter = ['course', 'author']

    class Meta:
        model = Post


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
