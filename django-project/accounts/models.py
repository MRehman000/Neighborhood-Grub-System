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
