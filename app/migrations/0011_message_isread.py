# Generated by Django 2.1.4 on 2019-01-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190121_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='isRead',
            field=models.BooleanField(default=False),
        ),
    ]
