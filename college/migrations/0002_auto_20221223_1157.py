# Generated by Django 2.2 on 2022-12-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userform',
            name='email',
            field=models.EmailField(default='i', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userform',
            name='password',
            field=models.CharField(default='r@gmail.com', max_length=20),
            preserve_default=False,
        ),
    ]
