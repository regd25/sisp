# Generated by Django 3.1.1 on 2020-10-09 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecStatus', '0005_auto_20201009_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geocolumn',
            name='isConnection',
        ),
    ]
