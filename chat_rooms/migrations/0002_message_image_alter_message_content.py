# Generated by Django 5.1.5 on 2025-01-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chat_images/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
