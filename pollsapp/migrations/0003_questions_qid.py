# Generated by Django 3.2.5 on 2021-11-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0002_auto_20211128_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='qid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
