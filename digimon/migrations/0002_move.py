# Generated by Django 5.1.1 on 2024-09-12 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digimon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
