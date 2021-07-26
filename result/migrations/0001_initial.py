# Generated by Django 3.2.5 on 2021-07-26 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('stupid', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('dumb', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Total_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stupid', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('dumb', models.IntegerField(default=0)),
            ],
        ),
    ]