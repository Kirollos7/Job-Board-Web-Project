# Generated by Django 3.0.7 on 2020-06-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20200623_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0, null=True),
        ),
    ]