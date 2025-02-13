from django.contrib import admin

from blog.models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title', )
    ordering = ('id', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'views', 'difficulty', 'reading_time')
    list_display_links = ('title', )
    list_filter = ('category', 'created_at', 'difficulty')
    ordering = ('id', )



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

