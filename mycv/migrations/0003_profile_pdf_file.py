# Generated by Django 5.0.1 on 2024-02-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0002_alter_profile_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pdf_file',
            field=models.FileField(default=1, upload_to='pdf'),
            preserve_default=False,
        ),
    ]