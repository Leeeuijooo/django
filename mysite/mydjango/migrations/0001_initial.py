# Generated by Django 4.1.6 on 2023-02-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('pictureurl', models.CharField(max_length=50)),
            ],
        ),
    ]
