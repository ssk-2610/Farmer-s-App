# Generated by Django 3.0.4 on 2020-03-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('passwd', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=20)),
                ('buyorsell', models.TextField(max_length=10)),
            ],
        ),
    ]
