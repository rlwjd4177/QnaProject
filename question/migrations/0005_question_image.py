# Generated by Django 3.0.5 on 2020-05-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20200530_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='answer/'),
        ),
    ]
