# Generated by Django 4.2.13 on 2024-06-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0002_alter_attractions_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='attractions',
            name='urls',
            field=models.URLField(blank=True, null=True),
        ),
    ]