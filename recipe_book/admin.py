from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status','created_on')
    search_fields = ['title']
    list_filter = ('status', 'author', 'created_on')  # Add multiple filters
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields ='__all__'
    class Media:
        css = {
            'all': ('summernote/summernote-bs4.css',)
        }
        js = ('summernote/summernote-bs4.js',)


admin.site.register(Comment)
