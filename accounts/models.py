from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .managers import UserManager
from iranian_cities.fields import OstanField, ShahrField


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن")
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="ایمیل")
    name = models.CharField(max_length=300, blank=True, null=True, verbose_name="نام")
    family_name = models.CharField(max_length=300, blank=True, null=True, verbose_name="نام خانوادگی")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="عکس پروفایل")
    state = models.CharField(max_length=300, blank=True, null=True, verbose_name="استان")
    city = models.CharField(max_length=300, blank=True, null=True, verbose_name="شهر")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_admin = models.BooleanField(default=False, verbose_name="ادمین")
    is_staff = models.BooleanField(default=False, verbose_name="کارمند")
    is_seller = models.BooleanField(default=False, verbose_name='فروشنده')

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'name', 'family_name']

    def __str__(self):
        return self.phone_number

    def get_full_name(self):
        return f'{self.name} {self.family_name}'

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Otp_Code(models.Model):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')
    code = models.IntegerField(unique=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'کد احراز هویت'
        verbose_name_plural = 'کدهای احراز هویت'

    def __str__(self):
        return f'{self.phone_number} {self.code} {self.created}'


class ProvinceAndCity(models.Model):
    province = OstanField()
    city = ShahrField()
