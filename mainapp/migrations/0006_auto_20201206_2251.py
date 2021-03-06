# Generated by Django 3.0.5 on 2020-12-06 22:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_diplomaprojectfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='diplomaproject',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diplomaproject',
            name='grade',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
