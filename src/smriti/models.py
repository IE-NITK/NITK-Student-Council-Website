from django.db import models
from django_markdown.models import MarkdownField
from django.conf import settings

# Create your models here.

class Testimonial(models.Model):
    testimonial_to = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="receiver")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="sender")
    timestamp = models.DateTimeField(auto_now_add=True)
    description = MarkdownField()

    def __str__(self):
        return "%s to %s" % (self.created_by.get_full_name(),self.testimonial_to.get_full_name())
