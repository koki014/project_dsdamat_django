# Generated by Django 3.1.4 on 2020-12-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20201222_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='choices_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='choices_categories', to='menu.Menu'),
        ),
    ]