# Generated by Django 3.2.15 on 2022-09-30 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cim_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('position', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
            ],
        ),
    ]
