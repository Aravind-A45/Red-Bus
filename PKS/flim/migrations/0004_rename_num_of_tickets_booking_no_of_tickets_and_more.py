# Generated by Django 4.2.4 on 2023-09-11 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flim', '0003_remove_route_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Num_of_tickets',
            new_name='No_of_tickets',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='Schedule',
            new_name='Schedule_id',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='User',
            new_name='User_id',
        ),
    ]
