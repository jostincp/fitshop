# Generated by Django 4.2.1 on 2023-05-22 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejemplo',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ejemplo',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='ejemplo',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]