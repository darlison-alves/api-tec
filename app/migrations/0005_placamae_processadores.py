# Generated by Django 3.0 on 2019-12-15 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191215_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='placamae',
            name='processadores',
            field=models.ManyToManyField(to='app.Processador'),
        ),
    ]
