# Generated by Django 5.1.3 on 2024-11-24 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PowerUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('powerup_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
