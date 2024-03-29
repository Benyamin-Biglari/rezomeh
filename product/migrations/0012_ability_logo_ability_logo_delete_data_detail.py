# Generated by Django 5.0 on 2023-12-28 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_remove_data_detail_logo_data_detail_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ability_logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('adress', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ability',
            name='logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.ability_logo'),
        ),
        migrations.DeleteModel(
            name='data_detail',
        ),
    ]
