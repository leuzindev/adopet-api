import re

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    TUTOR = 1
    ORG = 2
    USER_ROLES = (
        (TUTOR, 'Tutor'),
        (ORG, 'Membro de Organização'),
    )

    username = models.CharField(
        _('username'),
        max_length=15,
        unique=True,
        validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                _('Enter a valid username.'),
                _('invalid'))]
    )
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        _('last name'),
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        _('email address'),
        max_length=255,
        unique=True
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
    )

    date_joined = models.DateTimeField(
        _('date joined'),
        default=timezone.now
    )
    avatar = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
            validators.RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
            ),
        ],
    )
    about = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    role = models.PositiveSmallIntegerField(
        'Role',
        choices=USER_ROLES,
        default=TUTOR
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)

            if self.role == self.TUTOR:
                Tutor.objects.create(user=self)
            elif self.role == self.ORG:
                Organization.objects.create(user=self)
        else:
            old_role = User.objects.get(pk=self.pk).role

            if self.role != old_role:
                if old_role == self.TUTOR:
                    self.tutor.delete()
                    Organization.objects.create(user=self)
                elif old_role == self.ORG:
                    self.organization.delete()
                    Tutor.objects.create(user=self)

            super().save(*args, **kwargs)


class Tutor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


class Organization(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
