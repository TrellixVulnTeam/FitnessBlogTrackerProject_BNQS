# Generated by Django 2.2.4 on 2020-12-21 15:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FitnessBlog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postings',
            new_name='Post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content_of_post',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_of_post',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_of_post',
            new_name='title',
        ),
    ]
