# Generated by Django 2.2.1 on 2019-07-31 13:02

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190731_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=utilities.helper.Helper.slider_image_upload),
        ),
    ]
