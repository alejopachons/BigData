# Generated by Django 2.1.5 on 2019-02-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_delete_operation'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.IntegerField(verbose_name='Número 1')),
                ('number2', models.IntegerField(verbose_name='Número 2')),
            ],
        ),
    ]
