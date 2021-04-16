from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Items, Member
from django.contrib.auth.models import Group


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id","name", "price", "thumbnail")
    list_display_links = ("id","name", "price", "thumbnail")


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            "fields": ("email", "profile_pic", "first_name", "last_name", "state")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_superuser", "is_staff")
        })
    )
    add_fieldsets = (
        (None, {
            "fields": ("email", "profile_pic", "first_name", "last_name", "state")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_superuser", "is_staff")
        })
    )
    list_display = ["email", "first_name", "last_name", "state"]
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


admin.site.register(User, UserAdmin)
admin.site.register(Items, ItemAdmin)
admin.site.register(Member)
admin.site.unregister(Group)