# Generated by Django 4.0.6 on 2022-07-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0005_alter_speaker_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
