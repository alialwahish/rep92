# Generated by Django 2.0.5 on 2018-05-21 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('applogReg', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='username',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='date_of_birth',
            new_name='dob',
        ),
        migrations.AddField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
