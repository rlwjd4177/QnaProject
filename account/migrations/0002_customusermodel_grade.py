# Generated by Django 3.0.6 on 2020-06-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='grade',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
