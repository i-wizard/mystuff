# Generated by Django 2.2.1 on 2019-12-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0011_auto_20191119_0721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('closed_at',)},
        ),
        migrations.RenameField(
            model_name='attempt',
            old_name='team_a_score',
            new_name='total_score',
        ),
        migrations.RemoveField(
            model_name='attempt',
            name='team_b_score',
        ),
        migrations.RemoveField(
            model_name='question',
            name='team_a_score',
        ),
        migrations.RemoveField(
            model_name='question',
            name='team_b_score',
        ),
        migrations.AddField(
            model_name='question',
            name='total_score',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='total score'),
        ),
    ]
