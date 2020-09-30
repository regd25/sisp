# Generated by Django 3.1.1 on 2020-09-25 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clusters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MecStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last    modified', verbose_name='modified')),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clusters.well')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TRstate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last    modified', verbose_name='modified')),
                ('startMd', models.FloatField(max_length=10)),
                ('startTvd', models.FloatField(max_length=10)),
                ('endMd', models.FloatField(max_length=10)),
                ('endTvd', models.FloatField(max_length=10)),
                ('programType', models.CharField(choices=[('plan', 'plan'), ('real', 'real')], default='plan', max_length=4, verbose_name='Type of program')),
                ('pipeDiameter', models.CharField(choices=[('20', '20'), ('13 3/8', '13 3/8'), ('9 5/8', '9 5/8'), ('7', '7')], default='20', max_length=7)),
                ('drillDiameter', models.CharField(choices=[('26', '26'), ('16', '16'), ('12 1/4', '12 1/4'), ('8 1/2', '8 1/2')], default='26', max_length=7)),
                ('mecStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecStatus.mecstatus')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeoColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last    modified', verbose_name='modified')),
                ('startMd', models.FloatField(max_length=10)),
                ('startTvd', models.FloatField(max_length=10)),
                ('endMd', models.FloatField(max_length=10)),
                ('endTvd', models.FloatField(max_length=10)),
                ('programType', models.CharField(choices=[('plan', 'plan'), ('real', 'real')], default='plan', max_length=4, verbose_name='Type of program')),
                ('layer', models.CharField(choices=[('T.A', 'T.A'), ('RPLCN', 'RPLCN'), ('PLCNM', 'PLCNM'), ('PLCNS', 'PLCNS'), ('PL', 'PL'), ('MS', 'MS'), ('YAC-8', 'YAC-8'), ('YAC-7', 'YAC-7'), ('YAC-6', 'YAC-6'), ('YAC-5', 'YAC-5'), ('YAC-4', 'YAC-4'), ('YAC-3', 'YAC-3'), ('YAC-2', 'YAC-2'), ('YAC-1', 'YAC-1')], default='T.A', max_length=7, verbose_name='GeologicalLayer')),
                ('mecStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecStatus.mecstatus')),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
