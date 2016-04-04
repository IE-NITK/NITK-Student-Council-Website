from django.db import models
from django_markdown.models import MarkdownField
from django.conf import settings

# Create your models here.

class Testimonial(models.Model):
    description = MarkdownField()
    testimonial_to = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="receiver")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="sender")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s to %s" % (created_by,testimonial_to)
