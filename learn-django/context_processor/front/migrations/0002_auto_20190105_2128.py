# Generated by Django 2.0 on 2019-01-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='username',
            name='username',
            field=models.CharField(max_length=10),
        ),
    ]