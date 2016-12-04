from django.contrib import admin
from django.contrib.auth.models import User

from accounts.models import ChefPermissionsRequest, RedFlag, Complaint
from accounts.models import TerminateAccountRequest, CreateAccountRequest

from dishes.models import Diner

@admin.register(CreateAccountRequest)
class CreateAccountRequestAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Approve/Reject Create Account
    Request functionality.
    """
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "status",
        "user"
    ]
    actions = ["approve_request", "reject_request"]

    def get_queryset(self, request):
        """
        Limit the CreateAccountRequest queryset to those that are pending.
        """
        qs = super(CreateAccountRequestAdmin, self).get_queryset(request)
        return qs.filter(status=CreateAccountRequest.PENDING)

    def approve_request(self, request, queryset):
        """
        Create an account for each approved Create Account Request.
        """
        for createAccountRequest in queryset:
            # Create the User object.
            # Generate a random password
            password = User.objects.make_random_password()
            pass_file = "{}_password.txt".format(createAccountRequest.username)
            with open(pass_file, "w") as fh:
                print(password, file=fh)
            # "email" the person their random password. For this project that
            # will simply be printing the random password to stdout
            username = createAccountRequest.username
            email = createAccountRequest.email
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            # Create Diner object.
            diner = Diner.objects.create(user=user)
            # Update the status of this Create Account Request
            createAccountRequest.status = CreateAccountRequest.APPROVED
            createAccountRequest.save()

    def reject_request(self, request, queryset):
        """
        Set the status of each rejected request to rejected.
        """
        for createAccountRequest in queryset:
            createAccountRequest.status = CreateAccountRequest.REJECTED
            createAccountRequest.save(update_fields=["status"])

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

@admin.register(RedFlag)
class RedFlagAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Review Red Flag functionality.
    """
    actions = ["close_red_flag"]

    def close_red_flag(self, request, queryset):
        print("Rut rut rut rut")

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Review Complaint functionality.
    """
    actions = ["close_complaint"]

    def close_complaint(self, request, queryset):
        print("Woop woop woop woop")

@admin.register(TerminateAccountRequest)
class TerminateAccountRequestAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Delete User Account
    functionality.
    """
    list_display = ["user"]
    actions = ["delete_account"]

    def delete_account(self, request, queryset):
        for terminateAccountRequest in queryset:
            user = terminateAccountRequest.user
            user.delete()
