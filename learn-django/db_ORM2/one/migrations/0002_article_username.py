# Generated by Django 2.0 on 2018-12-10 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('two', '0001_initial'),
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='two.Front'),
        ),
    ]