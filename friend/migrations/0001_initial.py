# Generated by Django 4.2.6 on 2023-11-22 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=100)),
            ],
            options={
                'verbose_name': 'hello',
                'verbose_name_plural': 'hellos',
            },
        ),
    ]
