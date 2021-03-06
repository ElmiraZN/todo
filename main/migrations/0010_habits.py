# Generated by Django 4.0 on 2021-12-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_tomeet_date_of_meeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('done_for_today', models.BooleanField(default=False)),
                ('important', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=100)),
            ],
        ),
    ]
