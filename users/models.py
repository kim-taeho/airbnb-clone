from django.contrib.auth.models import AbstractUser
from django.db import models
from core import managers as core_managers
from django.conf import settings
import uuid
from django.shortcuts import reverse
from django.core.mail import send_mail


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANG_ENG = "en"
    LANG_KOR = "kr"

    LANG_CHOICES = ((LANG_ENG, "English"), (LANG_KOR, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANG_CHOICES, max_length=2, blank=True, default="KR"
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default="KRW"
    )
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    objects = core_managers.CustomModelManager()
    
    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail(
                "Verify Account Message",
                f"Verify Account, your secret: {secret}",
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=True,
            )
        return
