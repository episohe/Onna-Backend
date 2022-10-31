from django.db import models

from config.settings import AUTH_USER_MODEL


class CoreModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Agency(models.Model):
    """Real-estate Agency"""
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='회원')
    company = models.CharField(max_length=20, verbose_name='회사')
    ceo = models.CharField(max_length=20, verbose_name='대표')
    business_number = models.IntegerField(blank=True, null=True)
    businessRegistration = models.FileField()
    businessStatus = models.CharField(max_length=30)
    item = models.CharField(max_length=30)
    officerNumber = models.IntegerField(blank=True, null=True)
    officeCertificate = models.FileField()
    address = models.CharField(max_length=300, null=True)
    faxNumber = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')

    class Meta:
        db_table = 'agency'

    def __str__(self):
        return self.company

# class RealtyType(models.Model):
#     """
#     ASSETS_CHOICES = (
#     (0, '아파트'),
#     (1, '오피스텔'),
#     (2, '빌라'),
#     (3, '주택'),
#     (4, '원룸'),
#     (5, '상가'),
#     (6, '사무실'),
#     (7, '숙박'),
#     (8, '펜션'),
#     (9, '전원 주택'),
#     (10, '공장/창고'),
#     (11, '상업용 건물'),
#     (12, '분양권'),
#     (13, '재개발'),
#     (14, '토지'),
# )
#     """
#     type = models.CharField(max_length=50, verbose_name='매물 종류')
#
#     class Meta:
#         db_table = 'realty_type'
#         ordering = ['id']
#
#     def __str__(self):
#         return self.type
#
#
# class Enum:
#     PHONE_AGENCY_CHOICES = (
#         ('SKT', 'SKT'),
#         ('KT', 'KT'),
#         ('LG', 'LG'),
#         ('SKT 알뜰폰', 'SKT 알뜰폰'),
#         ('KT 알뜰폰', 'KT 알뜰폰'),
#         ('LG 알뜰폰', 'LG 알뜰폰'),
#     )
#
#     TRANSACTION_CHOICES = (
#         ('매매', '매매'),
#         ("월세", '월세'),
#         ("전세", '전세'),
#         ("반전세", '반전세'),
#         ("연세", '연세'),
#     )
#
#     STATE_CHOICES = (
#         ('접수', '접수'),
#         ('계약 중', '계약 중'),
#         ('계약 완료', '계약 완료'),
#     )
#
#
# class SaleNote(CoreModel):
#     # users = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name="SaleNoteUser")
#     transaction_type = models.CharField(max_length=20, choices=Enum.TRANSACTION_CHOICES, verbose_name='거래 종류')
#     realty_type = models.ForeignKey(RealtyType, blank=True, null=True, on_delete=models.CASCADE, verbose_name='매물 종류')
#     address = models.CharField(max_length=140, blank=True, null=True, verbose_name='주소')
#     price = models.IntegerField(default=0, blank=True, null=True, verbose_name='매매가')
#     deposit = models.IntegerField(default=0, blank=True, null=True, verbose_name='보증금')
#     rent = models.IntegerField(default=0, blank=True, null=True, verbose_name='월세')
#     owner = models.CharField(max_length=140, blank=True, null=True, verbose_name='소유자')
#     phone_agency = models.CharField(max_length=20, choices=Enum.PHONE_AGENCY_CHOICES, verbose_name='통신사')
#     owner_number = models.CharField(max_length=25, blank=True, null=True, verbose_name='소유자 연락처')
#     remarks = models.TextField(null=True, verbose_name='비고')
#     state = models.CharField(max_length=20, default='접수', choices=Enum.STATE_CHOICES, verbose_name='거래 상태')
#     # lessee_number = models.CharField(max_length=25, blank=True, null=True, verbose_name='임차인 연락처')
#     public_or_not = models.BooleanField(default=True, verbose_name='공개 여부')
#
#     def __str__(self):
#         return self.owner
#
#     @property
#     def realty_type_name(self):
#         return self.realty_type.type
#
#     class Meta:
#         ordering = ["pk"]
#         db_table = 'sale_note'
#
#
# class BuyingNote(CoreModel):
#     # users = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name="BuyingNoteUser")
#     transaction_type = models.CharField(max_length=20, choices=Enum.TRANSACTION_CHOICES, verbose_name='거래 종류')
#     realty_type = models.ForeignKey(RealtyType, blank=True, null=True, on_delete=models.CASCADE, verbose_name='매물 종류')
#     district = models.CharField(max_length=140, blank=True, null=True, verbose_name='희망 지역')
#     price = models.IntegerField(default=0, blank=True, null=True, verbose_name='매매가')
#     deposit = models.IntegerField(default=0, blank=True, null=True, verbose_name='보증금')
#     rent = models.IntegerField(default=0, blank=True, null=True, verbose_name='월세')
#     remarks = models.TextField(null=True, verbose_name='비고')
#     client = models.CharField(max_length=20, blank=True, null=True, verbose_name='고객')
#     phone_number = models.CharField(max_length=25, blank=True, null=True, verbose_name='연락처')
#     state = models.CharField(max_length=20, default='접수', choices=Enum.STATE_CHOICES, verbose_name='거래 상태')
#
#     def __str__(self):
#         return self.client
#
#     @property
#     def realty_type_name(self):
#         return self.realty_type.type
#
#     class Meta:
#         ordering = ["pk"]
#         db_table = 'buying_note'
