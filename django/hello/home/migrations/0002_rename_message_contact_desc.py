# Generated by Django 4.2.3 on 2023-07-21 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='desc',
        ),
    ]
