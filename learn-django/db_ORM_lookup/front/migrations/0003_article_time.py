# Generated by Django 2.0 on 2018-12-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20181213_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]