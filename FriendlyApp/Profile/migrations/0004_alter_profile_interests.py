# Generated by Django 3.2.7 on 2021-10-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_auto_20210927_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
