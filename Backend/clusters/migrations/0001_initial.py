# Generated by Django 3.1.1 on 2020-09-25 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last    modified', verbose_name='modified')),
                ('name', models.CharField(max_length=30)),
                ('contract', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last    modified', verbose_name='modified')),
                ('name', models.CharField(max_length=30)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clusters.cluster')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last    modified', verbose_name='modified')),
                ('name', models.CharField(max_length=40)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clusters.equipment')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
