from django.contrib import admin

from .models import Credential


@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    fields = [
        "note",
        "test_net",
    ]
    list_display = [
        "id",
        "user",
        "exchange",
        "test_net",
        "note",
        "created_at",
        "modified_at",
    ]
    list_select_related = ["user"]
    readonly_fields = [
        "user",
        "exchange",
        "created_at",
        "modified_at",
    ]
