from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .countries import COUNTRIES


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name=_("email address"), max_length=255, unique=True)
    is_staff = models.BooleanField(
        verbose_name=_("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active status"), default=True, help_text=_("Designates if the user can log in.")
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    first_name = models.CharField(
        max_length=255, default="", blank=True, verbose_name=_("first name")
    )
    last_name = models.CharField(
        max_length=255, default="", blank=True, verbose_name=_("last name")
    )
    address = models.CharField(max_length=100, default="", blank=True, verbose_name="adresse")
    city = models.CharField(max_length=40, default="", blank=True, verbose_name="ville")
    zip = models.CharField(max_length=12, default="", blank=True, verbose_name="code postal")
    country = models.CharField(
        max_length=2, choices=COUNTRIES, default="", blank=True, verbose_name="pays"
    )
    expertise = models.CharField(max_length=50, default="", blank=True)
    organization = models.CharField("Organisation", max_length=255, default="", blank=True)
    receives_emails = models.BooleanField(verbose_name="Reçoit les emails", default=True)

    USERNAME_FIELD = "email"
