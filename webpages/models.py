from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()  # Short description (used on service list page)
    detailed_description = models.TextField(blank=True, null=True)  # For service detail page
    features = models.TextField(blank=True, null=True)  # Optional: Comma-separated bullet points
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)  # e.g. Bootstrap icon name like 'bi-gear-fill'
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def feature_list(self):
        return [f.strip() for f in self.features.split(',')] if self.features else []

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