# Generated by Django 3.0.6 on 2020-06-03 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200603_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='grade',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
