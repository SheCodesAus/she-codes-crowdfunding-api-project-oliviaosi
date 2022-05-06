# Generated by Django 4.0.2 on 2022-05-06 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_rename_support_pledge_supporter'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='avatar',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]