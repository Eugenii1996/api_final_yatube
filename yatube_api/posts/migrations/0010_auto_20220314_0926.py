# Generated by Django 2.2.16 on 2022-03-14 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20220314_0919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pub_date'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]