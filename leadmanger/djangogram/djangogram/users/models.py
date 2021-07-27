from typing import BinaryIO
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import get_supported_language_variant, gettext_lazy as _


class User(AbstractUser):
    """Default user for djangogram."""

    # (DB저장값, 사용자입력값)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom'),
    ]
    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    # 사용자 이름 : char형(빈칸 가능, 최대 글자수가 255)
    user_name = models.CharField(blank=True, max_length=255)

    # 프로필 사진 : image형
    profile_photo = models.ImageField(blank=True)

    # 웹사이트 : url형 
    website = models.URLField(blank=True)

    # 소개 : text형
    bio = models.TextField(blank=True)

    # 이메일 : char형
    email = models.CharField(blank=True, max_length=255)

    # 전화번호 : char형
    phone_number = models.CharField(blank=True, max_length=255)

    # 성별 : char형(chice를 사용하여 특정값만 입력되도록)
    gender = models.CharField(blank=True, choices=GENDER_CHOICES, max_length=255)

    # 팔로워(다대다관계)
    followers = models.ManyToManyField("self")
    # 팔로잉(다대다관계)
    following = models.ManyToManyField("self")

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
