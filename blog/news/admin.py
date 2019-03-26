from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


class CommentsAdmin(SummernoteModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')
    summernote_fields = ('text',)


admin.site.register(News, NewsAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comments, CommentsAdmin)

