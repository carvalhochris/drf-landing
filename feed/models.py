from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField()

    def __str__(self):
        return self.title

class Page(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    featured_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    description = models.TextField()
    call_to_action = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    # other fields for your landing page model
