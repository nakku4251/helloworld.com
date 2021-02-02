from django.db import models
from django.utils import timezone
# Create your models here.

class Diary(models.Model):
    category = models.CharField("カテゴリ", max_length=225)
    text = models.TextField("本文")
    created_at = models.DateTimeField("作成日", default=timezone.now)
