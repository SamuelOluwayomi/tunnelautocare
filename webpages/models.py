from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField("Full Name", max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.created_at.strftime('%Y-%m-%d')})"
    
class Review(models.Model):
    fullname = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)  # 1–5 stars
    created_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)  # Admin approval

    def __str__(self):
        return f"{self.fullname} ({self.rating}★)"