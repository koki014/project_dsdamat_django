# Generated by Django 3.1.4 on 2020-12-26 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201226_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title_ar',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title_az',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title_it',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title_tr',
        ),
    ]