# Generated by Django 5.0.4 on 2024-04-24 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='profile_picture/'),
        ),
    ]
