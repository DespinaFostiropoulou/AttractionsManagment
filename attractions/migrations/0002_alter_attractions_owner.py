# Generated by Django 4.2.13 on 2024-06-13 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attractions', to=settings.AUTH_USER_MODEL),
        ),
    ]
