# Generated by Django 2.2 on 2021-10-10 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_auto_20211010_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdetails',
            name='status',
        ),
        migrations.AlterField(
            model_name='bookdetails',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bookdetails',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
