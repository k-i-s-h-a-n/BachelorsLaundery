# Generated by Django 4.0.6 on 2022-11-08 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='Phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='desc',
        ),
    ]
