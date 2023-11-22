from django.contrib.admin import register, ModelAdmin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Post, Category


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = (
        'pk',
        'pub_date',
        'author',
        'categories',

    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = (
        'title',
        'slug',
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('slug',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'