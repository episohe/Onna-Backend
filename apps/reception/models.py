from django.db import models


class Reception(models.Model):
    """매수장"""

    TRANSACTION_CHOICES = (
        ('1', '매매'),
        ('2', '전세'),
        ('3', '월세'),
    )

    name = models.CharField(verbose_name="이름", max_length=10)
    phone = models.CharField(verbose_name="연락처", max_length=20)
    transaction_type = models.IntegerField(verbose_name="거래 종류", choices=TRANSACTION_CHOICES)
    region = models.CharField(verbose_name="희망 지역", max_length=100, null=True, blank=True)
    memo = models.TextField(verbose_name="비고", null=True, blank=True)

    class Meta:
        db_table = "reception"

    def transaction_type_name(self):
        return self.get_transaction_type_display()
