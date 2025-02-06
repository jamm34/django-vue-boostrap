from django.contrib import admin

from .models import Comment


# Register your models here.
#adminnistrar clases empleando decoradores


class CommentAdmin(admin.ModelAdmin):
    # list_display = ('id', 'text',)
    # search_fields = ('id', 'text',)
    # date_hierarchy = 'date_posted'
    # ordering = ('date_posted',)
    # list_filter = ('id', )
    # list_editable = ('text',)
    #fields = ('text',)
    #exclude = ('element',)
    pass

admin.site.register(Comment, CommentAdmin)