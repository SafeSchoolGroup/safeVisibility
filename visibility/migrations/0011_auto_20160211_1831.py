# Generated by Django 2.1.3 on 2016-02-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visibility', '0010_auto_20160211_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etablissement',
            name='nom',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
