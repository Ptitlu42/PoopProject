from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number):
        if not phone_number:
            raise ValueError('Phone number is required')
        user = self.model(phone_number=phone_number)
        user.save(using=self._db)

    def delete_user (self, phone_number):
        if not phone_number:
            raise ValueError('Phone number is required')
        user = self.model(phone_number=phone_number)
        user.delete()

    def update_user (self, phone_number, name, password, mail):
        if not phone_number:
            raise ValueError('Phone number is required')
        user = self.model(phone_number=phone_number)
        user.save()

    def get_user(self, phone_number):
        if not phone_number:
            raise ValueError('Phone number is required')
        user = self.model(phone_number=phone_number)
        return user

class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    mail = models.EmailField(unique=True)
    user_since = models.DateTimeField(auto_now_add=True)
    total_draw = models.IntegerField(default=0)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return self.name
