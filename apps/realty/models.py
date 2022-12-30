from django.contrib.auth import get_user_model
from django.db import models

from core.models import CoreModel


class Realty(CoreModel):
    """매물장"""

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

    PHONE_AGENCY_CHOICES: tuple = (
        (1, 'SKT'),
        (2, 'KT'),
        (3, 'LGU+'),
        (4, 'SKT 알뜰폰'),
        (5, 'KT 알뜰폰'),
        (6, 'LGU+ 알뜰폰'),
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
        related_name="realty_user"
    )

    client_name = models.CharField(verbose_name="소유자 성함", max_length=10)
    client_phone = models.CharField(verbose_name="소유자 연락처", max_length=20)
    phone_agency = models.IntegerField(verbose_name="통신사", choices=PHONE_AGENCY_CHOICES, null=True)
    lessee_phone = models.CharField(verbose_name="임차인 연락처", max_length=20)
    transaction_type = models.IntegerField(verbose_name="거래 종류", choices=TRANSACTION_CHOICES)
    property_type = models.IntegerField(verbose_name="부동산 종류", choices=PROPERTY_CHOICES)
    region = models.CharField(verbose_name="지역", max_length=100, null=True, blank=True)
    price = models.IntegerField(verbose_name="매매가", default=0)
    deposit = models.IntegerField(verbose_name="보증금", default=0)
    monthly_rent = models.IntegerField(verbose_name="월세", default=0)
    state = models.IntegerField(choices=STATE_CHOICES, verbose_name="진행 단계", default=1)
    memo = models.TextField(verbose_name="비고", null=True, blank=True)

    class Meta:
        db_table = "realty"

    def transaction_type_name(self):
        return self.get_transaction_type_display()

    def property_type_name(self):
        return self.get_property_type_display()

    def phone_agency_name(self):
        return self.get_phone_agency_display()

    def state_name(self):
        return self.get_state_display()
