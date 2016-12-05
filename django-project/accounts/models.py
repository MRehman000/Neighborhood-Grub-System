import decimal

from django.db import models
from django.contrib.auth.models import User

class CreateAccountRequest(models.Model):
    """
    Django class representing a Create Account Request.

    Attributes:

    user:
        The User object created as a result of this request being approved.

    username:
        The username for the account, if it is created.

    first name:
        The first name of the person applying for an NGS account.

    last name:
        The last name of the person applying for an NGS account.

    email:
        The email the person wishes to associate with this account. The email
        must be unique

    latitude:
        The default latitude coordinate for this account.

    longitude:
        The default longitude coordinates for this account.

    status:
        The status of this account. Status descriptions are given below.

        pending:
            A system administrator has yet to review this request and take an
            action on it.
        approved:
            A system administrator has approved this request.
        rejected:
            A system administrator has rejected this request.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    latitude = models.DecimalField(max_digits=9,
                                   decimal_places=6,
                                   default=decimal.Decimal(0.0))
    longitude = models.DecimalField(max_digits=9,
                                    decimal_places=6,
                                    default=decimal.Decimal(0.0))

    PENDING, APPROVED, REJECTED = 0, 1, 2

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (REJECTED, "Rejected")
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)



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

    user:
    first_dish_name:
    first_dish_image:
    second_dish_name:
    second_dish_image:
    third_dish_name:
    third_dish_image:
    video_biography:

    status:
        The status of this account. Status descriptions are given below.

        pending:
            A system administrator has yet to review this request and take an
            action on it.
        approved:
            A system administrator has approved this request.
        rejected:
            A system administrator has rejected this request.
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

    PENDING, APPROVED, REJECTED = 0, 1, 2

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (APPROVED, "Approved"),
        (REJECTED, "Rejected")
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)

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

class Complaint(models.Model):
    """
    Django class representing a complaint made by one user against another.

    Attributes:

    complainant:
        The user making the complaint against the complainee.

    complainee:
        The user the complaint is being made against.

    description:
        A description of the complaint the complainant is making.

    status:
        The status of this complaint. Status descriptions are given below.

        Pending:
            A superuser has not yet decided how to resolve this Complaint.
        Closed:
            A superuser has reviewed this Complaint and the issue has been
            closed.
    """
    complainant = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name="complaint_allegation")
    complainee = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name="complaint_receipt")
    description = models.TextField("Complaint Description")

    PENDING, CLOSED = 0, 1

    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (CLOSED, "Closed")
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)
