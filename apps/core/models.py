from django.db import models


class CoreModel(models.Model):
    created = models.DateTimeField(verbose_name="생성일", auto_now_add=True)
    modified = models.DateTimeField(verbose_name="수정일", auto_now=True)

    class Meta:
        abstract = True
