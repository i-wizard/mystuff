# Generated by Django 2.2.1 on 2019-07-12 21:35

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=utilities.helper.Helper.slider_image_upload)),
                ('should_show', models.BooleanField(default=False)),
            ],
        ),
    ]