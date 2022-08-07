from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

from .validators import validate_no_special_characters


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, organization, password):

        if not email:
            raise ValueError('must have users email')
        if not password:
            raise ValueError('must have users password')

        user = self.model(
            email=self.normalize_email(email),
            organization=organization
        )
        user.set_password(password)
        user.save(using=self._db)
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


class Agency(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(
        max_length=255,
        unique=True,
        error_messages={'unique': '이미 사용 중인 이메일 입니다.'}
    )
    organization = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    userId = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용 중인 아이디 입니다.'},
    )

    name = models.CharField(
        max_length=10,
        null=True,
        validators=[validate_no_special_characters],
    )

    phoneNumber = models.CharField(
        default="000-0000-0000",
        max_length=15,
        null=True,
        unique=True
    )

    # 업체 정보

    company = models.CharField(max_length=20)
    ceoName = models.CharField(max_length=10)
    businessNumber = models.IntegerField(blank=True, null=True)
    businessRegistration = models.FileField()
    businessStatus = models.CharField(max_length=30)
    item = models.CharField(max_length=30)
    officerNumber = models.IntegerField(blank=True, null=True)
    officeCertificate = models.FileField()

    address = models.CharField(
        max_length=40,
        null=True,
        validators=[validate_no_special_characters],
    )

    faxNumber = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['organization']

    class Meta:
        db_table = 'agency'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

# profile_pic = models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')
