from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """This class helps Django work with the custom user Model."""

    def create_user(self, email, name, password=None):
        """This method creates a user."""
        if not email:
            raise ValueError("The user must provide an email address")

        email = self.normalize_email(email)
        user  = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user
        
    def create_super_user(self, email, name, password):
        """This functions creates super user and save him/her with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff     = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile inside our system."""

    email       = models.EmailField(max_length=255, unique=True)
    name        = models.CharField(max_length=255)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)

    objects     = UserProfileManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """This function grabs the users fullname and returns it when it is called!!!!"""
        return self.name

    def get_short_name(self):
        """This functions grabs the users short name and returns it when it is called!!!!
        it can be first or last name
        """
        return self.name

    def __str__(self):
        """This method returns a string name of the object."""
        return self.email

