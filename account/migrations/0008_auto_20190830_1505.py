# Generated by Django 2.2.1 on 2019-08-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190827_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='transaction_status',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='request_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
