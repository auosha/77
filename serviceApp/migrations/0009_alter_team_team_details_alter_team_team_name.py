# Generated by Django 4.0.3 on 2022-08-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0008_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_details',
            field=models.TextField(verbose_name='Detail'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=250, verbose_name='Name'),
        ),
    ]
