# Generated by Django 2.2 on 2020-12-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2019-12-20'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
