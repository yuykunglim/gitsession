# Generated by Django 3.1.7 on 2021-03-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0002_content_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='boolean',
            field=models.BooleanField(default=False),
        ),
    ]
