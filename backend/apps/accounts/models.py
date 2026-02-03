from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import random
import string


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    '''Кастомная модель пользователя'''
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        if not self.username:  # Only generate username if it's not already set
            self.username = self.generate_unique_username()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    @staticmethod
    def generate_unique_username():
        """Generate a unique username in the format 'user' + random digits"""
        while True:
            username = 'user' + ''.join(random.choices(string.digits, k=6))
            if not User.objects.filter(username=username).exists():
                return username