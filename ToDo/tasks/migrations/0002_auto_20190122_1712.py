# Generated by Django 2.1.5 on 2019-01-22 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tasks',
            new_name='task',
        ),
    ]