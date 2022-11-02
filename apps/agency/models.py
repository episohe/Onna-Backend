from django.db import models


class Agency(models.Model):
    """Agency model"""

    name = models.CharField(max_length=50, verbose_name='회사 이름')
    address = models.CharField(max_length=255, verbose_name='주소')
    contact = models.CharField(max_length=255, verbose_name='연락처')

    class Meta:
        db_table = "agency"
        verbose_name = "회사"
