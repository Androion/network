# Generated by Django 2.1.2 on 2018-11-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='createdDate',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='createdDate',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='createdDate',
            new_name='created_date',
        ),
    ]