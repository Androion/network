# Generated by Django 2.1.2 on 2018-11-07 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20181107_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=256, verbose_name='작성자'),
        ),
    ]
