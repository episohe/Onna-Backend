# Generated by Django 4.1 on 2022-12-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0004_alter_realty_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realty',
            name='phone_agency',
            field=models.IntegerField(choices=[(1, 'SKT'), (2, 'KT'), (3, 'LGU+'), (4, 'SKT 알뜰폰'), (5, 'KT 알뜰폰'), (6, 'LGU+ 알뜰폰')], null=True, verbose_name='통신사'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, '매매'), (2, '전세'), (3, '월세')], verbose_name='거래 종류'),
        ),
    ]