# Generated by Django 3.1.3 on 2021-01-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20210103_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='college',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='qpapers',
            name='college',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='qpapers',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
