# Generated by Django 4.0.6 on 2022-07-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0008_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='motivation',
            field=models.TextField(null=True),
        ),
    ]
