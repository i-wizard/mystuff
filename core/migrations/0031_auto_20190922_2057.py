# Generated by Django 2.2.1 on 2019-09-22 19:57

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20190904_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=utilities.helper.Helper.slider_image_upload),
        ),
    ]
