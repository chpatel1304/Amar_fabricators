# Generated by Django 5.0.6 on 2024-06-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_career_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='cv',
            field=models.FileField(upload_to='cvs/'),
        ),
    ]
