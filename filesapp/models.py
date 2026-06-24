from django.core.exceptions import ValidationError
from django.db import models


def validate_file(value):
    allowed_extensions = ['pdf', 'xlsx']

    ext = value.name.split('.')[-1].lower()

    if ext not in allowed_extensions:
        raise ValidationError(
            'Разрешены только PDF и XLSX файлы'
        )


class Document(models.Model):
    title = models.CharField(max_length=255)

    file = models.FileField(
        upload_to='documents/',
        validators=[validate_file]
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title