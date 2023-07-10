from django.contrib import admin

# Register your models here.
from . models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment_date', 'comment_text', 'comment_sign', 'comment_contact', 'answer_for_comment',
                    'answer_sign']
    list_display_links = ['comment_text']
    search_fields = ['comment_date', 'comment_text', 'comment_sign', 'comment_contact', 'answer_for_comment',
                     'answer_sign']


admin.site.register(Comments, CommentsAdmin)