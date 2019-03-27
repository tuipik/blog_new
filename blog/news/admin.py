from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ('title', 'category', 'published',)
    list_editable = ["published", ]


class CommentsAdmin(SummernoteModelAdmin):
    list_display = ('user', 'new', 'created',)
    summernote_fields = ('text',)


admin.site.register(News, NewsAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comments, CommentsAdmin)

