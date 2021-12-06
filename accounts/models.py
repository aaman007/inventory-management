from django.contrib.auth.models import AbstractUser as BaseUser, UserManager as BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    pass


class User(BaseUser):
    objects = UserManager()

    class Meta:
        ordering = ['-id']
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return self.get_full_name()
