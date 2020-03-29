# Generated by Django 2.2.6 on 2020-03-29 14:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('activity_periods_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('end_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('real_name', models.CharField(default=None, max_length=100)),
                ('tz', models.CharField(default=None, max_length=100)),
                ('activity_periods', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.ActivityPeriod')),
            ],
        ),
    ]