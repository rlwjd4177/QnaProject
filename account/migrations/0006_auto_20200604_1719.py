# Generated by Django 3.0.6 on 2020-06-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_customusermodel_last_signed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='point',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
