# Generated by Django 4.0.3 on 2022-03-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkedinusers',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]