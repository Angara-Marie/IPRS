# Generated by Django 4.1.2 on 2022-10-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('middle_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('id_number', models.IntegerField()),
            ],
        ),
    ]