# Generated by Django 4.2.5 on 2024-01-04 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_logo_my_work_range_delete_title_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_work_range',
            name='logo',
        ),
        migrations.DeleteModel(
            name='logo',
        ),
    ]
