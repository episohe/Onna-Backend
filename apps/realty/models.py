# Create your models here.
# 아파트/오피스텔/분양권/빌라/주택/원룸/상가/사무실/숙박/펜션/전원 주택/공장 및 창고/상업용 건물
# 재개발/토지

# 전세/월세/연세/매매

# 아파트 -> 단지/동 층수/ 방수/욕실/관리비/매물 특징
from django.db import models


class RealtyType(models.Model):
    """
    ASSETS_CHOICES = (
    (0, '아파트'),
    (1, '오피스텔'),
    (2, '빌라'),
    (3, '주택'),
    (4, '원룸'),
    (5, '상가'),
    (6, '사무실'),
    (7, '숙박'),
    (8, '펜션'),
    (9, '전원 주택'),
    (10, '공장/창고'),
    (11, '상업용 건물'),
    (12, '분양권'),
    (13, '재개발'),
    (14, '토지'),
)
    """
    type = models.CharField(max_length=50, verbose_name='매물 종류')

    class Meta:
        db_table = 'realty_type'
        ordering = ['id']

    def __str__(self):
        return self.type
