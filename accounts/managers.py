from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,phone_number,email, name,family_name,password):
        if not phone_number:
            raise ValueError('Phone number must be set')
        if not email:
            raise ValueError('Email must be set')
        if not name:
            raise ValueError('Name must be set')
        if not family_name:
            raise ValueError('Family name must be set')
        user=self.model(phone_number=phone_number,email=self.normalize_email(email),name=name,family_name=family_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,phone_number,email,name,family_name,password):
        user= self.create_user(phone_number,email,name,family_name,password)
        user.is_admin = True
        user.is_staff=True
        user.is_superuser = True
        user.save(using=self.db)
        return user
