import jsonfield
from django.db import models
from django_cryptography.fields import encrypt
from model_utils.models import TimeStampedModel

# Create your models here.


class PromptLog(TimeStampedModel):

    prompt = jsonfield.JSONField(max_length=2000)
    result = models.CharField(max_length=200)
    tokens = models.CharField(max_length=200)
    response = jsonfield.JSONField(default=dict, blank=True, null=True)
    sensitive_data = encrypt(models.CharField(max_length=50, blank=True, null=True))
                                                

    # PromptLog methods
    def __str__(self):
        return self.prompt
