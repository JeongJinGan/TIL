# Generated by Django 3.2.13 on 2022-09-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20220928_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
