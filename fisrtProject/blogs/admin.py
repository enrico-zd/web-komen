from django.contrib import admin
from .models import Blogs, Comment

# membuat inline untuk komentar, apa yang mau diselipkan
class CommentInline(admin.StackedInline):
	model = Comment

class BlogAdmin(admin.ModelAdmin):
	inlines = [CommentInline, ]


# Register your models here.
admin.site.register(Blogs, BlogAdmin)

# # kita bisa menambahkan model comment di ke admin dengan cara
# admin.site.register(Comment)