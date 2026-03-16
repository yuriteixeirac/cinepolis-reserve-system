from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
       

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not username or not email:
            raise ValidationError('No identifiyng credentials were passed.')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email, username=username
        )
        user.set_password(password)
        user.save()

        return user
        

class User(AbstractBaseUser):
    class Meta:
        db_table = 'users'

    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]
