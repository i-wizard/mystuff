# Generated by Django 2.2.1 on 2019-07-12 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0002_auto_20190712_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='events',
        ),
    ]