from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4'], message='Faqat mp4 formatdagi videolar!')
    ], help_text=".mp4 formatdagi videolar!")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def validate_file_size(value):
  limit_size = 10485760
  if value.size > limit_size:
    raise ValidationError(f'Fayl hajmi juda katta ({limit_size // 1024 // 1024} MB)')


class File(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='files/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'jpg', 'png'],
                               message='Faqat mp4, jpg, png formatdagi fayllar!'),
        validate_file_size
    ])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
