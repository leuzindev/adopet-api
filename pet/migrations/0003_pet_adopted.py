# Generated by Django 4.2.6 on 2023-10-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_alter_pet_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='adopted',
            field=models.BooleanField(default=False),
        ),
    ]
