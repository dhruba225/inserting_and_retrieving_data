# Generated by Django 4.2.3 on 2023-08-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='access_record',
            name='email',
            field=models.EmailField(default='dhru225@gmail.com', max_length=254),
        ),
    ]
