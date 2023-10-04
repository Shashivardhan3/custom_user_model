from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Provide the email')
        email=self.normalize_email(email)
        email=email.lower()
        user=self.model(email=email,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,first_name,last_name,password):
        User=self.create_user(email,first_name,last_name,password)
        User.is_superuser=True
        User.is_staff=True
        User.save()
        return User


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
    objects=UserProfileManager()

        
    def __str__(self):
        return self.first_name+" "+self.last_name
    

