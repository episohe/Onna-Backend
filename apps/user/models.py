from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_field):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, organization, password):
        user = self.create_user(
            email=self.normalize_email(email),
            organization=organization,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User"""

    PERMISSION_CHOICES: tuple = (
        ('Subscriber', '구독자'),
        ('User', '일반 사용자')
    )

    email = models.EmailField(verbose_name='이메일', unique=True)
    name = models.CharField(verbose_name='이름', max_length=20)
    phone = models.CharField(verbose_name='연락처', max_length=30, unique=True)
    organization = models.CharField(verbose_name='소속', max_length=50)
    role = models.CharField(verbose_name='직급/직책', max_length=30)
    is_active = models.BooleanField(verbose_name='', default=True)
    is_admin = models.BooleanField(verbose_name='이름', default=False)
    permission = models.CharField(verbose_name='권한', max_length=10, choices=PERMISSION_CHOICES, default='User')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['organization']

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
