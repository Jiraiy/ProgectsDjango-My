# Generated by Django 2.1.4 on 2019-01-05 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190105_0736'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choise',
            new_name='Choice',
        ),
    ]
