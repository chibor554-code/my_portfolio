from django.contrib import admin
from .models import Contact, Skill, Post, Profile

from .models import Project
admin.site.register(Project)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("name", "email", "subject", "message")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level",
        "proficiency",
        "order",
    )
    list_editable = (
        "proficiency",
        "order",
    )
    ordering = ("order", "name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "author",
    )
    search_fields = (
        "title",
        "content",
    )
    prepopulated_fields = {
        "slug": ("title",)
    }
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "profession",
        "email",
        "phone",
        "location",
    )

    search_fields = (
        "full_name",
        "profession",
        "email",
        "location",
    )

    list_filter = (
        "location",
        "profession",
    )