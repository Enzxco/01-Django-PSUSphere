# Generated by Django 5.1.6 on 2025-03-06 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentorg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='college_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='program',
            name='prog_name',
            field=models.CharField(max_length=150),
        ),
    ]
