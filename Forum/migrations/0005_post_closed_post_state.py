# Generated by Django 4.2.3 on 2023-07-27 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0004_reply_comment_post_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.CharField(default='zero', max_length=40),
        ),
    ]
