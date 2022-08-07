from django.db import models

from core.models import CoreModel
from realty.models import RealtyType


class Enum:
    PHONE_AGENCY_CHOICES = (
        ('SKT', 'SKT'),
        ('KT', 'KT'),
        ('LG', 'LG'),
        ('SKT 알뜰폰', 'SKT 알뜰폰'),
        ('KT 알뜰폰', 'KT 알뜰폰'),
        ('LG 알뜰폰', 'LG 알뜰폰'),
    )

    TRANSACTION_CHOICES = (
        ('매매', '매매'),
        ("월세", '월세'),
        ("전세", '전세'),
        ("반전세", '반전세'),
        ("연세", '연세'),
    )

    STATE_CHOICES = (
        ('접수', '접수'),
        ('계약 중', '계약 중'),
        ('계약 완료', '계약 완료'),
    )


class SaleNote(CoreModel):
    # users = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name="SaleNoteUser")
    transaction_type = models.CharField(max_length=20, choices=Enum.TRANSACTION_CHOICES, verbose_name='거래 종류')
    realty_type = models.ForeignKey(RealtyType, blank=True, null=True, on_delete=models.CASCADE, verbose_name='매물 종류')
    address = models.CharField(max_length=140, blank=True, null=True, verbose_name='주소')
    price = models.IntegerField(default=0, blank=True, null=True, verbose_name='매매가')
    deposit = models.IntegerField(default=0, blank=True, null=True, verbose_name='보증금')
    rent = models.IntegerField(default=0, blank=True, null=True, verbose_name='월세')
    owner = models.CharField(max_length=140, blank=True, null=True, verbose_name='소유자')
    phone_agency = models.CharField(max_length=20, choices=Enum.PHONE_AGENCY_CHOICES, verbose_name='통신사')
    owner_number = models.CharField(max_length=25, blank=True, null=True, verbose_name='소유자 연락처')
    remarks = models.TextField(null=True, verbose_name='비고')
    state = models.CharField(max_length=20, default='접수', choices=Enum.STATE_CHOICES, verbose_name='거래 상태')
    # lessee_number = models.CharField(max_length=25, blank=True, null=True, verbose_name='임차인 연락처')
    public_or_not = models.BooleanField(default=True, verbose_name='공개 여부')

    def __str__(self):
        return self.owner

    @property
    def realty_type_name(self):
        return self.realty_type.type

    class Meta:
        ordering = ["pk"]
        db_table = 'sale_note'


class BuyingNote(CoreModel):
    # users = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name="BuyingNoteUser")
    transaction_type = models.CharField(max_length=20, choices=Enum.TRANSACTION_CHOICES, verbose_name='거래 종류')
    realty_type = models.ForeignKey(RealtyType, blank=True, null=True, on_delete=models.CASCADE, verbose_name='매물 종류')
    district = models.CharField(max_length=140, blank=True, null=True, verbose_name='희망 지역')
    price = models.IntegerField(default=0, blank=True, null=True, verbose_name='매매가')
    deposit = models.IntegerField(default=0, blank=True, null=True, verbose_name='보증금')
    rent = models.IntegerField(default=0, blank=True, null=True, verbose_name='월세')
    remarks = models.TextField(null=True, verbose_name='비고')
    client = models.CharField(max_length=20, blank=True, null=True, verbose_name='고객')
    phone_number = models.CharField(max_length=25, blank=True, null=True, verbose_name='연락처')
    state = models.CharField(max_length=20, default='접수', choices=Enum.STATE_CHOICES, verbose_name='거래 상태')

    def __str__(self):
        return self.client

    @property
    def realty_type_name(self):
        return self.realty_type.type

    class Meta:
        ordering = ["pk"]
        db_table = 'buying_note'
