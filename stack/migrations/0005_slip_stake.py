# Generated by Django 2.2.1 on 2019-07-14 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0004_auto_20190714_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='slip',
            name='stake',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=17),
        ),
    ]
