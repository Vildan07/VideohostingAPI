# Generated by Django 5.0.6 on 2024-06-13 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='saver.category'),
            preserve_default=False,
        ),
    ]
