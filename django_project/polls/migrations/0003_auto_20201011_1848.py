# Generated by Django 3.1.2 on 2020-10-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201011_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='dt_published',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
