# Generated by Django 2.0.5 on 2018-05-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applogReg', '0013_auto_20180521_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='user_fav_quotes',
        ),
        migrations.AddField(
            model_name='quotes',
            name='user_fav_quotes',
            field=models.ManyToManyField(related_name='user_fav_quotes', to='applogReg.Users'),
        ),
        migrations.DeleteModel(
            name='join',
        ),
    ]
