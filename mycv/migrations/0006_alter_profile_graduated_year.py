# Generated by Django 5.0.1 on 2024-02-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0005_alter_profile_experience_alter_profile_previous_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Graduated_year',
            field=models.DateField(blank=True),
        ),
    ]
