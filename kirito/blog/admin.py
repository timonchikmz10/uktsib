from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

class PostInline(admin.StackedInline):
    model = models.IntoPost
    extra = 1

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "create_at", "author"]
    inlines = [PostInline]
    save_as = True
    save_on_top = True

@admin.register(models.IntoPost)
class IntoPostAdmin(admin.ModelAdmin):
    list_display = ["name", "about"]

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
