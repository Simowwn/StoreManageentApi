# Generated by Django 5.1.6 on 2025-02-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
    ]
