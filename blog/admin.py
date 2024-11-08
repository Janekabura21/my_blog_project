from django.contrib import admin
from .models import Post

# Register the Post model with the admin panel
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('author', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Post, PostAdmin)

