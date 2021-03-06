# Generated by Django 2.2.2 on 2021-05-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('session_token', models.CharField(default=0, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
