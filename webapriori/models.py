from django.core.validators import FileExtensionValidator
from django.db import models


class Csv(models.Model):
    """model for products"""

    csv = models.FileField(
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["csv"])],
    )
    min_support = models.FloatField()
    uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded"]
