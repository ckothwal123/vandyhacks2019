# Generated by Django 2.2.5 on 2019-11-03 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='characters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_characters', models.IntegerField()),
                ('Character_1', models.CharField(max_length=30)),
                ('gender_1', models.CharField(max_length=30)),
                ('Character_2', models.CharField(max_length=30)),
                ('gender_2', models.CharField(max_length=30)),
                ('Character_3', models.CharField(max_length=30)),
                ('gender_3', models.CharField(max_length=30)),
                ('Character_4', models.CharField(max_length=30)),
                ('gender_4', models.CharField(max_length=30)),
                ('Character_5', models.CharField(max_length=30)),
                ('gender_5', models.CharField(max_length=30)),
            ],
        ),
    ]