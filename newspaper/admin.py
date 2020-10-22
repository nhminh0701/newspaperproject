from django.contrib import admin
from newspaper import models




@admin.register(models.Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)



class SubcategoryInline(admin.StackedInline):
    model = models.Subcategory
    extra = 1



@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SubcategoryInline,
    ]



class CommentInline(admin.TabularInline):
    model = models.Comment
    extra = 1



class ReplyInline(admin.TabularInline):
    model = models.Reply
    extra = 1



@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    list_filter = ('category', 'subcategory', 'author', 'created_at')
    inlines = [
        CommentInline,
    ]



@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'created_at', 'votes')
    list_filter = ('article', 'user', 'created_at')
    inlines = [
        ReplyInline,
    ]



@admin.register(models.Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'created_at', 'votes')
    list_filter = ('comment', 'user', 'created_at')