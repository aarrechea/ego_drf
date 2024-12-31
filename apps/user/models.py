# Imports
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from apps.abstract.models import AbstractModel, AbstractManager




# User manager
class UserManager(BaseUserManager, AbstractManager):
    def create_user(self, email, password=None, **kwargs):
        if email is None:
            raise TypeError("Users must have an email")
        if password is None:
            raise TypeError("Users must have a password")
        
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)        
        return user
        
        
    def create_superuser(self, email, password, **kwargs):
        if email is None:
            raise TypeError("Superusers must have an email")
        if password is None:
            raise TypeError("Superusers must have a password")
        
        user = self.create_user(email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



# File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
def user_directory_path(instance, filename):    
    return "user_{0}/{1}".format(instance.public_id, filename)



# User type
USER_TYPE = (
    (1,'Super Admin'),
    (2,'Admin'),
    (3,'Player')
)



# User model
class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=70)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)    
    photo = models.ImageField(null=True, blank=True, upload_to=user_directory_path)    
    user_type = models.IntegerField(choices=USER_TYPE, default=3)
    is_verified = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    
    def __str__(self):
        return f"Username: {self.email}"
    
    
    # To be accessed anywhere on a User object
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"



