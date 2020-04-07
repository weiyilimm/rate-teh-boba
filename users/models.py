from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    first_name = models.CharField(max_length=30,null='true', blank='true')
    last_name = models.CharField(max_length=30,null='true', blank='true')
    bio = models.TextField(null='true', blank='true')

    def __str__(self):
        return f'{self.user.username} Profile'


