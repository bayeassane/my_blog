from django.contrib import admin
from .models import Post, Category

class PostAdminInline(admin.StackedInline):
    model = Post
    extra = 1
    verbose_name = 'article'
    verbose_name_plural = 'articles'



# class admin.Model
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, ({'fields': ['name']}))
    ]

    inlines = [PostAdminInline]
    

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ['created_at', 'category']
    search_fields = ['title']

# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
