from blog.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin) :
	list_display = ('title', 'created_at')

# Register your models here.
admin.site.register(Post, PostAdmin)
