# Generated by Django 5.0 on 2023-12-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_work_work_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='work_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_work_place', models.CharField(max_length=150, null=True)),
                ('email', models.EmailField(max_length=150, null=True)),
                ('phone_number', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
