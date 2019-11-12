# Generated by Django 2.2.7 on 2019-11-12 15:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0003_auto_20191112_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
    ]
