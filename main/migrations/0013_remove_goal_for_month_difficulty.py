# Generated by Django 4.0 on 2022-01-09 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_goal_for_month_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal_for_month',
            name='difficulty',
        ),
    ]
