# Generated by Django 3.2.7 on 2021-09-11 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('middleware', '0004_userips_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userips',
            name='date_created',
        ),
    ]