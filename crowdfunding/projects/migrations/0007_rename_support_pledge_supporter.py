# Generated by Django 4.0.2 on 2022-05-01 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pledge',
            old_name='support',
            new_name='supporter',
        ),
    ]
