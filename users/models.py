from django.db import models
from django.contrib.auth.models import (AbstractUser, PermissionsMixin, BaseUserManager, 
UserManager as AbstractUserManager,AbstractBaseUser)
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """ This replaces the default User model. """
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='images/%Y/%m/%d', default="images/avatar.jpg", blank=True)
    state = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name', 'profile_pic', 'state']

    class Meta:
        ordering = ('date_joined',)

    def __str__(self):
        return self.email


class Member(models.Model):
    """ This model registers an interested member. """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey("Items", related_name="members", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.email


class Items(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=252)
    user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE, null=True)
    thumbnail = models.ImageField(upload_to='pictures/%Y/%m/%d', default="images/avatar.jpg")
    interest = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # This allows only one post to be featured.
        if self.featured:
            try:
                temp = Items.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Items.DoesNotExist:
                pass
   
        super(Items, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def get_members(self):
        return self.members.all().order_by("-timestamp")

