from django.contrib.auth import get_user_model
from django.db import models


class Reception(models.Model):
    """매수장"""

    TRANSACTION_CHOICES: tuple = (
        (1, '매매'),
        (2, '전세'),
        (3, '월세'),
    )

    PROPERTY_CHOICES: tuple = (
        (1, '아파트'),
        (2, '빌라'),
        (3, '상가'),
        (4, '공장/창고'),
        (5, '오피스텔'),
        (6, '원룸')
    )

    STATE_CHOICES: tuple = (
        (1, '접수'),
        (2, '계약 중'),
        (3, '계약 완료'),
    )

    user = models.ForeignKey(
        verbose_name="회원",
        to=get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name="reception_user"
    )

    client_name = models.CharField(verbose_name="이름", max_length=10)
    client_phone = models.CharField(verbose_name="연락처", max_length=20)
    transaction_type = models.IntegerField(verbose_name="거래 종류", choices=TRANSACTION_CHOICES)
    property_type = models.IntegerField(verbose_name="부동산 종류", choices=PROPERTY_CHOICES)
    region = models.CharField(verbose_name="희망 지역", max_length=100, null=True, blank=True)
    price = models.IntegerField(verbose_name="매매가", default=0)
    deposit = models.IntegerField(verbose_name="보증금", default=0)
    monthly_rent = models.IntegerField(verbose_name="월세", default=0)
    state = models.IntegerField(choices=STATE_CHOICES, verbose_name="진행 단계", default=1)
    memo = models.TextField(verbose_name="비고", null=True, blank=True)

    class Meta:
        db_table = "reception"

    def transaction_type_name(self):
        return self.get_transaction_type_display()

    def property_type_name(self):
        return self.get_property_type_display()

    def state_name(self):
        return self.get_state_display()
