from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .managers import UserManager


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن")
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="ایمیل")
    name = models.CharField(max_length=300, blank=True, null=True, verbose_name="نام")
    family_name = models.CharField(max_length=300, blank=True, null=True, verbose_name="نام خانوادگی")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    state = models.CharField(max_length=300, blank=True, null=True, verbose_name="استان")
    city = models.CharField(max_length=300, blank=True, null=True, verbose_name="شهر")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیرفعال")
    is_admin = models.BooleanField(default=False, verbose_name="ادمین / عادی")
    is_staff = models.BooleanField(default=False, verbose_name="کارمند / عادی")
    is_seller = models.BooleanField(default=False, verbose_name='فروشنده / عادی')

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'name','family_name']

    def __str__(self):
        return self.phone_number

    def get_full_name(self):
        return f'{self.name} {self.family_name}'

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
