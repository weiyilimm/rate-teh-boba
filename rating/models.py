from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Cafe(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20, default='city')
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='images/')

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify( self.title)
        super(Cafe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE,
                             blank=True, null=True, related_name='feedbacks')
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cafe.title
