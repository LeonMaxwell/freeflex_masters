# Generated by Django 4.0.1 on 2022-01-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='count_rated',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]