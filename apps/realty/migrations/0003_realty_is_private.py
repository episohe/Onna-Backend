# Generated by Django 4.1.4 on 2022-12-13 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0002_realty_created_realty_modified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='realty',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='비공개 여부'),
        ),
    ]
