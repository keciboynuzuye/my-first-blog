from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ['title']
    #exclude = ('created_date',)
    readonly_fields = ('created_date',)
#admin.site.register(User)
admin.site.register(Post,PostAdmin)
