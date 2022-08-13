# Generated by Django 4.1 on 2022-08-07 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('transaction_type', models.CharField(choices=[('매매', '매매'), ('월세', '월세'), ('전세', '전세'), ('반전세', '반전세'), ('연세', '연세')], max_length=20, verbose_name='거래 종류')),
                ('address', models.CharField(blank=True, max_length=140, null=True, verbose_name='주소')),
                ('price', models.IntegerField(blank=True, default=0, null=True, verbose_name='매매가')),
                ('deposit', models.IntegerField(blank=True, default=0, null=True, verbose_name='보증금')),
                ('rent', models.IntegerField(blank=True, default=0, null=True, verbose_name='월세')),
                ('owner', models.CharField(blank=True, max_length=140, null=True, verbose_name='소유자')),
                ('phone_agency', models.CharField(choices=[('SKT', 'SKT'), ('KT', 'KT'), ('LG', 'LG'), ('SKT 알뜰폰', 'SKT 알뜰폰'), ('KT 알뜰폰', 'KT 알뜰폰'), ('LG 알뜰폰', 'LG 알뜰폰')], max_length=20, verbose_name='통신사')),
                ('owner_number', models.CharField(blank=True, max_length=25, null=True, verbose_name='소유자 연락처')),
                ('remarks', models.TextField(null=True, verbose_name='비고')),
                ('state', models.CharField(choices=[('접수', '접수'), ('계약 중', '계약 중'), ('계약 완료', '계약 완료')], default='접수', max_length=20, verbose_name='거래 상태')),
                ('public_or_not', models.BooleanField(default=True, verbose_name='공개 여부')),
                ('realty_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realty.realtytype', verbose_name='매물 종류')),
            ],
            options={
                'db_table': 'sale_note',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='BuyingNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('transaction_type', models.CharField(choices=[('매매', '매매'), ('월세', '월세'), ('전세', '전세'), ('반전세', '반전세'), ('연세', '연세')], max_length=20, verbose_name='거래 종류')),
                ('district', models.CharField(blank=True, max_length=140, null=True, verbose_name='희망 지역')),
                ('price', models.IntegerField(blank=True, default=0, null=True, verbose_name='매매가')),
                ('deposit', models.IntegerField(blank=True, default=0, null=True, verbose_name='보증금')),
                ('rent', models.IntegerField(blank=True, default=0, null=True, verbose_name='월세')),
                ('remarks', models.TextField(null=True, verbose_name='비고')),
                ('client', models.CharField(blank=True, max_length=20, null=True, verbose_name='고객')),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True, verbose_name='연락처')),
                ('state', models.CharField(choices=[('접수', '접수'), ('계약 중', '계약 중'), ('계약 완료', '계약 완료')], default='접수', max_length=20, verbose_name='거래 상태')),
                ('realty_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realty.realtytype', verbose_name='매물 종류')),
            ],
            options={
                'db_table': 'buying_note',
                'ordering': ['pk'],
            },
        ),
    ]