# Generated by Django 4.0 on 2021-12-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomeet',
            name='date_of_meeting',
            field=models.DateField(auto_now=True),
        ),
    ]
