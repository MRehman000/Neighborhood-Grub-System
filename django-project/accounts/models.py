from django.db import models
from django.contrib.auth.models import User

class CreateAccountRequest(models.Model):
    """
    Django class representing a Create Account Request.

    Attributes:

    first name:
        The first name of the person applying for an NGS account.

    last name:
        The last name of the person applying for an NGS account.

    email:
        The email the person wishes to associate with this account.

    location:
        The default location for the person's account.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    # TODO: Add location information.

class TerminateAccountRequest(models.Model):
    """
    Django class representing a Terminate Account Request.

    Attributes:

    user:
        The user who has requested that their account be terminated.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ChefPermissionsRequest(models.Model):
    """
    Django class representing a chef permissions request.

    Attributes:
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_dish_name = models.CharField(max_length=256)
    first_dish_image = models.ImageField(
        max_length=256,
        upload_to="chef-permissions-requests-uploads/"
    )

    second_dish_name = models.CharField(max_length=256)
    second_dish_image = models.ImageField(
        max_length=256,
        upload_to="chef-permissions-requests-uploads/"
    )

    third_dish_name = models.CharField(max_length=256)
    third_dish_image = models.ImageField(
        max_length=256,
        upload_to="chef-permissions-requests-uploads/"
    )

    video_biography = models.FileField(
        max_length=256,
        upload_to="chef-permissions-requests-uploads/"
    )

class Suggestion(models.Model):
    """
    Django class representing a suggestion made by a visitor or user to the
    site.

    Attributes:

    suggestion:
        The suggestion being made by the visitor or user.
    """
    suggestion = models.TextField()

class RedFlag(models.Model):
    """
    Django class representing a red flag that is raised on a user.

    Attributes:

    user:
        The user who is flagged by this RedFlag instance.

    status:
        The status of this RedFlag. Status descriptions are below.

        Pending:
            A superuser has not yet decided how to resolve this RedFlag.
        Closed:
            A superuser has reviewed this RedFlag and the issue has been
            closed.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    PENDING, CLOSED = 0, 1

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (CLOSED, "Closed")
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)
