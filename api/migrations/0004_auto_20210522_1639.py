# Generated by Django 2.2.2 on 2021-05-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210522_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='session_token',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
