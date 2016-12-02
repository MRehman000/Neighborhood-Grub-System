from django.contrib import admin
from accounts.models import ChefPermissionsRequest

@admin.register(ChefPermissionsRequest)
class ChefPermissionsRequestAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Grant/Deny Chef Permissions
    Request functionality.
    """
    actions = ["grant_request", "deny_request"]

    def grant_request(self, request, queryset):
        print("What what what what")

    def deny_request(self, request, queryset):
        print("Yut yut yut yut")
