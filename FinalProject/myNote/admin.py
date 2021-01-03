from django.contrib import admin
from django.contrib import admin
from django.utils.html import format_html

from .models import Notes

# Register your models here.
class noteAdmin(admin.ModelAdmin):

    # def thumbnail(self, object):
    #     """
    #         Similar to str.format, but pass all arguments through conditional_escape(),
    #         and call mark_safe() on the result. This function should be used instead
    #         of str.format or % interpolation to build up small HTML fragments.
    #
    #         """
    #     return format_html('<img src="{}" width="100px" style="border-radius:10%;"/>'.format(object.note_pic.url))

    list_display_links = ['name', 'text', 'added_on', 'updated_on']
    list_display = ('name', 'text','added_on','updated_on')

admin.site.register(Notes,noteAdmin)

