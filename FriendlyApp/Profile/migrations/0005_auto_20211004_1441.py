# Generated by Django 3.2.7 on 2021-10-04 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_alter_profile_interests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='food_preferences',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='interests',
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_activity',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_food',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
